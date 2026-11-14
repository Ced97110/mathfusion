"""Convert « Des nombres aux structures » (prose edition, PDF) into the site's chapters.
Zero tokens: pure script. Adapted from tools/ml/build.py (same page size, same method).

Usage (from the repo root):
    python3 tools/livre/build.py <book.pdf> [work_dir]
    LIVRE_ONLY=AP,1,13 python3 tools/livre/build.py ...   # rebuild some sections only (keys)

Writes:
    content/toc.json                  the 82 sections (AP, 1-80, A)
    public/chapters/chKEY.html        one HTML fragment per section
    public/chapters/img/chKEY/*.svg   formulas, tables and figures, cut out of the PDF

Plain text lines are reflowed as HTML. Anything else (figures, tables, stacked formulas)
is cut out of the PDF as a vector SVG band (PyMuPDF), so nothing of the book is rewritten.
"""
from __future__ import annotations

import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass, field

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ONLY = {k for k in os.environ.get('LIVRE_ONLY', '').split(',') if k}
SCALE = 1.5  # pdftohtml pixels per PDF point (108 dpi)
PAGE_W = 425
FOOTER_TOP = 722  # page numbers sit below this line
PARA_GAP = 25
INK_LEVEL = 170
NEAR = 4  # px around a text line searched for drawing ink
TEXT_LEFT = 25
BULLET = '•'


@dataclass
class Item:
    top: int
    left: int
    w: int
    h: int
    kind: str  # body | math | head | fig
    size: int
    text: str  # inner XML (escaped, may hold <i>/<b>)

    @property
    def bottom(self) -> int:
        return self.top + self.h


@dataclass
class Line:
    items: list[Item]

    @property
    def top(self) -> int:
        return min(i.top for i in self.items)

    @property
    def bottom(self) -> int:
        return max(i.bottom for i in self.items)

    @property
    def left(self) -> int:
        return min(i.left for i in self.items)

    @property
    def right(self) -> int:
        return max(i.left + i.w for i in self.items)

    def plain(self) -> bool:
        """One baseline: body text at body size, inline math (subscripts allowed)."""
        for i in self.items:
            if i.kind == 'body' and not 13 <= i.size <= 16:
                return False
            if i.kind == 'math' and not 7 <= i.size <= 17:
                return False
            if i.kind in ('head', 'fig'):
                return False
        for a, b in zip(self.items, self.items[1:]):
            gap = b.left - (a.left + a.w)
            if gap > 24 and not (a.text.strip() == BULLET and a is self.items[0]):
                return False  # table row: cells far apart
        body = [i for i in self.items if i.kind == 'body'] or self.items
        tops = [i.top for i in body]
        return max(tops) - min(tops) <= 3 and self.bottom - self.top <= 26


@dataclass
class Block:
    kind: str  # p | eq | h2 | cap | vis
    page: int
    top: int
    bottom: int
    lines: list[Line] = field(default_factory=list)
    left: int = 0
    right: int = 0
    li: bool = False  # bullet item
    page_start: bool = False


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def load_xml(pdf: str, work: str) -> ET.Element:
    os.makedirs(work, exist_ok=True)
    if not os.path.exists(f'{work}/all.xml'):
        run(['pdftohtml', '-xml', '-i', '-q', pdf, f'{work}/all'])
    src = open(f'{work}/all.xml', encoding='utf8').read()
    return ET.fromstring(re.sub(r'<!DOCTYPE[^>]*>', '', src))


def clean_title(t: str) -> str:
    return re.sub(r'\s+', ' ', t.strip().replace("'", '’'))


def outline(root: ET.Element) -> list[dict]:
    """The 82 sections: Avant-propos (AP), chapters 1-80, annex (A). The outline is flat."""
    out = []
    for el in root.find('outline'):
        if el.tag != 'item':
            continue
        title = clean_title(el.text or '')
        m = re.match(r'(\d+|A) (.*)', title)
        if m:
            out.append({'key': m.group(1), 'title': m.group(2), 'page': int(el.get('page'))})
        elif title.startswith('Avant-propos'):
            out.append({'key': 'AP', 'title': title.split(' : ', 1)[-1].capitalize() if ' : ' in title else title,
                        'page': int(el.get('page'))})
    return out


def kind_of(family: str, size: int, bold: bool) -> str:
    if 'LatinModernMath' in family:
        return 'math'
    if 'DejaVuSerif' in family:
        return 'head' if bold and size >= 16 else 'body'
    return 'fig'  # DejaVuSans, STIX, Cmsy, mono: labels drawn inside figures


def page_items(page: ET.Element, fonts: dict) -> list[Item]:
    items = []
    for t in page.iter('text'):
        inner = ET.tostring(t, encoding='unicode', method='xml')
        inner = re.sub(r'^<text[^>]*>', '', inner)
        inner = re.sub(r'</text>\s*$', '', inner)
        inner = re.sub(r'<a [^>]*>', '', inner).replace('</a>', '')
        top = int(t.get('top'))
        if top > FOOTER_TOP and re.fullmatch(r'[0-9ivxlc]+', re.sub('<[^>]+>', '', inner).strip()):
            continue  # page number
        size, fam = fonts[t.get('font')]
        bold = inner.startswith('<b>')
        items.append(Item(top, int(t.get('left')), int(t.get('width')), int(t.get('height')),
                          kind_of(fam, size, bold), size, inner))
    return items


def group_lines(items: list[Item]) -> list[Line]:
    ctr = lambda it: it.top + it.h / 2
    groups: list[list[Item]] = []
    for it in sorted(items, key=ctr):
        if groups and abs(ctr(it) - ctr(groups[-1][0])) <= 6:
            groups[-1].append(it)
        else:
            groups.append([it])
    return [Line(sorted(g, key=lambda i: i.left)) for g in groups]


def ink_rows(raster: np.ndarray, items: list[Item]) -> np.ndarray:
    """Rows holding ink outside every text box (rules, frames, figures, tables)."""
    ink = raster < INK_LEVEL
    mask = np.zeros_like(ink)
    for it in items:
        if it.kind == 'fig':
            continue  # figure labels count as part of the drawing
        mask[max(0, it.top - 3):it.bottom + 4, max(0, it.left - 2):it.left + it.w + 3] = True
    ink &= ~mask
    ink[FOOTER_TOP:] = False
    return ink.sum(axis=1) >= 2


def runs(flags: np.ndarray) -> list[tuple[int, int]]:
    out, start = [], None
    for y, f in enumerate(flags):
        if f and start is None:
            start = y
        elif not f and start is not None:
            out.append((start, y))
            start = None
    if start is not None:
        out.append((start, len(flags)))
    return out


def text_of(ln: Line) -> str:
    return re.sub('<[^>]+>', '', ''.join(i.text for i in ln.items)).strip()


def page_blocks(pn: int, items: list[Item], raster: np.ndarray) -> list[Block]:
    lines = group_lines(items)
    rows = ink_rows(raster, items)
    blocks: list[Block] = []
    for a, b in runs(rows):
        if b - a < 3:
            continue  # a lone horizontal rule carries nothing
        cols = np.where((raster[a:b] < INK_LEVEL).any(axis=0))[0]
        blocks.append(Block('vis', pn, a, b, left=int(cols.min()), right=int(cols.max()) + 1))
    stacked = set()
    for a, b in zip(lines, lines[1:]):
        if b.top < a.bottom - 3:
            stacked |= {id(a), id(b)}
    for ln in lines:
        txt = text_of(ln)
        hits = rows[max(0, ln.top - NEAR):ln.bottom + NEAR].any()
        if all(i.kind == 'head' for i in ln.items):
            kind = 'h2'
        elif ln.plain() and not hits and id(ln) not in stacked:
            if re.match(r'Fig\. [0-9A]+\.\d+', txt):
                kind = 'cap'
            elif all(i.kind == 'math' for i in ln.items) and ln.left > TEXT_LEFT + 20:
                kind = 'eq'  # displayed one-line formula
            else:
                kind = 'p'
        else:
            kind = 'vis'
        blocks.append(Block(kind, pn, ln.top, ln.bottom, [ln], ln.left, ln.right, li=txt.startswith(BULLET)))
    blocks.sort(key=lambda b: (b.top, b.kind != 'vis'))
    return merge(blocks)


def merge(blocks: list[Block]) -> list[Block]:
    """Join visual pieces that touch, heading lines, and text lines into paragraphs."""
    out: list[Block] = []
    for b in blocks:
        prev = out[-1] if out else None
        if prev and prev.kind == 'vis' and b.kind == 'vis' and b.top - prev.bottom < 28:
            absorb(prev, b)
        elif prev and prev.kind == 'vis' and b.top < prev.bottom:
            absorb(prev, b)
        elif prev and prev.kind == 'vis' and prev.lines and b.kind == 'p' and b.top - prev.bottom < 8:
            absorb(prev, b)  # wrapped table cell right under a ruled row
            b.kind = 'vis'
        elif prev and prev.kind == 'h2' and b.kind == 'h2' and b.top - prev.bottom < 12:
            absorb(prev, b)
        elif prev and prev.kind in ('p', 'cap') and b.kind == 'p' and continues(prev, b):
            absorb(prev, b)
        else:
            out.append(b)
    return out


def absorb(a: Block, b: Block) -> None:
    a.top, a.bottom = min(a.top, b.top), max(a.bottom, b.bottom)
    a.left, a.right = min(a.left, b.left), max(a.right, b.right)
    a.lines += b.lines


def continues(prev: Block, b: Block) -> bool:
    if b.li or b.top - prev.bottom > PARA_GAP - 14:
        return False
    if prev.li and b.lines[0].left < prev.lines[0].left + 10:
        return False  # back to the text margin after a bullet item
    return not (b.lines[0].left > prev.lines[-1].left + 25)


def line_html(ln: Line) -> str:
    big = [i for i in ln.items if i.size >= 13] or ln.items
    mid = sorted(i.top + i.h / 2 for i in big)[len(big) // 2]
    out, prev = [], None
    for i in ln.items:
        if prev is not None and i.left - (prev.left + prev.w) >= 2:
            out.append(' ')
        if i.kind == 'math' and i.size <= 12:
            tag = 'sub' if i.top + i.h / 2 > mid else 'sup'
            out.append(f'<{tag} class="m">{i.text}</{tag}>')
        elif i.kind == 'math':
            out.append(f'<span class="m">{i.text}</span>')
        else:
            out.append(i.text)
        prev = i
    return ''.join(out)


def join_lines(lines: list[str], vocab: set[str]) -> str:
    text = ''
    for s in lines:
        if not text:
            text = s
            continue
        m = re.search(r'(\w+)-$', text)
        n = re.match(r'([a-zà-ÿœ]+)', s)
        if m and n:
            joined = (m.group(1) + n.group(1)).lower()
            hyph = f'{m.group(1)}-{n.group(1)}'.lower()
            text = text[:-1] + s if (joined in vocab or hyph not in vocab) else text + s
            continue
        text += ' ' + s
    return re.sub(r'</i>\s*<i>', ' ', re.sub(r'</b>\s*<b>', ' ', text))


_DOCS: dict = {}


def svg_band(pdf: str, pn: int, x: int, y: int, w: int, h: int, dst: str) -> None:
    """Cut a band out of page pn as a vector SVG (coordinates in pdftohtml pixels).

    PyMuPDF, not pdftocairo: poppler 26.03 places the SVG crop clip at the wrong height.
    MuPDF writes the whole page into the SVG, so what lies outside the band is pruned.
    """
    import fitz  # PyMuPDF
    if pdf not in _DOCS:
        _DOCS[pdf] = fitz.open(pdf)
    doc = _DOCS[pdf]
    x0, y0 = math.floor(x / SCALE), math.floor(y / SCALE)
    x1, y1 = math.ceil((x + w) / SCALE), math.ceil((y + h) / SCALE)
    page = doc[pn - 1]
    page.set_cropbox(fitz.Rect(x0, y0, x1, y1) & page.mediabox)  # rounding may pass the edge
    src = page.get_svg_image(text_as_path=True)
    with open(dst, 'w', encoding='utf8') as fh:
        fh.write(round_svg(prune_svg(src, x1 - x0, y1 - y0)))


SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
NUM = re.compile(r'-?\d*\.?\d+(?:e-?\d+)?')


def svg_matrix(t: str | None) -> tuple[float, ...]:
    m = re.match(r'matrix\(([^)]*)\)', t or '')
    return tuple(float(v) for v in re.split(r'[ ,]+', m.group(1).strip())) if m else (1, 0, 0, 1, 0, 0)


def path_box(d: str, m: tuple[float, ...]) -> tuple[float, float, float, float] | None:
    """Bounding box of an absolute path (M L C Q H V Z, as MuPDF writes them)."""
    xs, ys, x, y = [], [], 0.0, 0.0
    for cmd, args in re.findall(r'([MLCHVZQ])([^MLCHVZQ]*)', d):
        v = [float(n) for n in NUM.findall(args)]
        pts = [(a, y) for a in v] if cmd == 'H' else [(x, b) for b in v] if cmd == 'V' else list(zip(v[0::2], v[1::2]))
        for x, y in pts:
            xs.append(m[0] * x + m[2] * y + m[4])
            ys.append(m[1] * x + m[3] * y + m[5])
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None


def prune_svg(src: str, w: float, h: float, pad: float = 2.0) -> str:
    """Drop glyphs and paths lying wholly outside the w x h viewport, then unused definitions."""
    root = ET.fromstring(src)
    defs = root.find(f'{{{SVG_NS}}}defs')

    def outside(b: tuple[float, float, float, float]) -> bool:
        return b[2] < -pad or b[0] > w + pad or b[3] < -pad or b[1] > h + pad

    def walk(parent: ET.Element) -> None:
        for el in list(parent):
            if el is defs:
                continue
            tag = el.tag.rsplit('}', 1)[-1]
            if tag == 'g':
                walk(el)
                if len(el) == 0:
                    parent.remove(el)
            elif tag == 'use':
                m = svg_matrix(el.get('transform'))
                size = abs(m[0]) + abs(m[1]) + abs(m[2]) + abs(m[3])
                if outside((m[4] - size, m[5] - size, m[4] + size, m[5] + size)):
                    parent.remove(el)
            elif tag == 'path':
                box = path_box(el.get('d', ''), svg_matrix(el.get('transform')))
                if box and outside(box):
                    parent.remove(el)

    walk(root)
    if defs is not None:
        root.remove(defs)
        body = ET.tostring(root, encoding='unicode')
        used = set(re.findall(r'#([\w-]+)', body))
        for el in list(defs):
            if el.get('id') and el.get('id') not in used:
                defs.remove(el)
        root.insert(0, defs)
    return ET.tostring(root, encoding='unicode')


def round_svg(src: str) -> str:
    """Keep 3 decimals and drop the data-text attributes: about a third lighter, no visible change."""
    def short(m: re.Match) -> str:
        v = f'{float(m.group()):.3f}'.rstrip('0').rstrip('.')
        return re.sub(r'^(-?)0\.', r'\1.', v) or '0'
    return re.sub(r' data-text="[^"]*"', '', re.sub(r'-?\d*\.\d{4,}', short, src))


def vocabulary(root: ET.Element) -> set[str]:
    words: Counter = Counter()
    for t in root.iter('text'):
        for w in re.findall(r"[a-zà-ÿœ]+(?:-[a-zà-ÿœ]+)*", ''.join(t.itertext()).lower()):
            words[w] += 1
    return set(words)


def pending_continues(pending: list[str], b: Block) -> bool:
    """A paragraph goes on across a page break unless the previous text ended a sentence."""
    if not b.page_start or b.li:
        return False
    last = re.sub('<[^>]+>', '', pending[-1]).rstrip()
    return not re.search(r'[.?!:»”]$', last)


def chapter_html(blocks: list[Block], key: str, pdf: str, outdir: str, vocab: set[str]) -> str:
    imgdir = f'{outdir}/img/ch{key}'
    shutil.rmtree(imgdir, ignore_errors=True)
    os.makedirs(imgdir)
    parts: list[str] = []
    pending: list[str] = []
    state = {'li': False, 'k': 0}

    def flush() -> None:
        if pending:
            text = join_lines(pending, vocab)
            if state['li']:
                item = re.sub(r'^•\s*', '', text)
                parts.append(f'<p class="li">{item}</p>')
            else:
                parts.append(f'<p>{text}</p>')
            pending.clear()

    for b in blocks:
        if b.kind == 'p':
            if pending and not pending_continues(pending, b):
                flush()
            if not pending:
                state['li'] = b.li
            pending.extend(line_html(ln) for ln in b.lines)
            continue
        flush()
        if b.kind == 'h2':
            head = re.sub(r'</?[bi]>', '', ' '.join(line_html(l) for l in b.lines))
            parts.append(f'<h2>{head}</h2>')
        elif b.kind == 'cap':
            parts.append(f'<p class="cap">{join_lines([line_html(l) for l in b.lines], vocab)}</p>')
        elif b.kind == 'eq':
            parts.append(f'<p class="eq">{line_html(b.lines[0])}</p>')
        else:
            state['k'] += 1
            x0, x1 = max(0, min(b.left, TEXT_LEFT) - 5), min(PAGE_W, max(b.right, 400) + 5)
            y0, y1 = max(0, b.top - 3), min(FOOTER_TOP, b.bottom + 3)
            name = f'p{b.page:04d}_{state["k"]}.svg'
            svg_band(pdf, b.page, x0, y0, x1 - x0, y1 - y0, f'{imgdir}/{name}')
            alt = html.escape(' '.join(re.sub('<[^>]+>', '', line_html(l)) for l in b.lines), quote=True)
            fig = any(i.kind == 'fig' for l in b.lines for i in l.items) or not b.lines
            parts.append(f'<img class="{"vf" if fig else "vm"}" src="/chapters/img/ch{key}/{name}" alt="{alt}" '
                         f'style="--w:{(x1 - x0) / 16:.2f}" loading="lazy">')
    flush()
    return '\n'.join(parts)


def drop_title(blocks: list[Block]) -> list[Block]:
    """Drop the heading at the top of the first page (« Chapitre N » and the title)."""
    out = list(blocks)
    while out and out[0].page == blocks[0].page and out[0].kind == 'h2' and out[0].top < 150:
        txt = ' '.join(text_of(l) for l in out[0].lines)
        if re.match(r'\d+\. ', txt):
            break  # first numbered section of the chapter
        out.pop(0)
    return out


def rasters(pdf: str, first: int, last: int, tmp: str) -> dict[int, np.ndarray]:
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    run(['pdftoppm', '-r', '108', '-gray', '-f', str(first), '-l', str(last), pdf, f'{tmp}/p'])
    out = {}
    for f in os.listdir(tmp):
        out[int(re.search(r'(\d+)\.pgm$', f).group(1))] = np.asarray(Image.open(os.path.join(tmp, f)))
    return out


def label_of(key: str) -> str:
    return 'Avant-propos' if key == 'AP' else 'Annexe' if key == 'A' else f'Chapitre {key}'


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = os.path.abspath(sys.argv[1])
    work = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else f'{ROOT}/book/livre-work')
    root = load_xml(pdf, work)
    sections = outline(root)
    if len(sections) != 82:
        sys.exit(f'plan inattendu : {len(sections)} sections au lieu de 82')
    pages = {int(p.get('number')): p for p in root.iter('page')}
    fonts: dict = {}
    for p in pages.values():
        for fs in p.iter('fontspec'):
            fonts[fs.get('id')] = (int(fs.get('size')), fs.get('family'))
    vocab = vocabulary(root)
    outdir = f'{ROOT}/public/chapters'
    os.makedirs(outdir, exist_ok=True)
    starts = [s['page'] for s in sections]
    tmp = tempfile.mkdtemp(prefix='livre-ras-')
    toc = []
    try:
        for i, s in enumerate(sections):
            key = s['key']
            file = f'ch{int(key):02d}.html' if key.isdigit() else f'ch{key}.html'
            toc.append({'key': key, 'file': file, 'title': s['title']})
            if ONLY and key not in ONLY:
                continue
            last = starts[i + 1] - 1 if i + 1 < len(starts) else max(pages)
            ras = rasters(pdf, s['page'], last, tmp)
            blocks: list[Block] = []
            for pn in range(s['page'], last + 1):
                bl = page_blocks(pn, page_items(pages[pn], fonts), ras[pn])
                if bl:
                    bl[0].page_start = True
                blocks += bl
            stem = file[:-5]
            body = chapter_html(drop_title(blocks), stem[2:], pdf, outdir, vocab)
            with open(f'{outdir}/{file}', 'w', encoding='utf8') as fh:
                fh.write(f'<div class="pk">{label_of(key)}</div>\n<h1>{html.escape(s["title"])}</h1>\n{body}')
            print(f'{key:>3}  p.{s["page"]:<5} {s["title"][:60]}', flush=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if not ONLY:
        with open(f'{ROOT}/content/toc.json', 'w', encoding='utf8') as fh:
            json.dump(toc, fh, ensure_ascii=False)
    print('livre :', len(toc), 'sections')


if __name__ == '__main__':
    main()
