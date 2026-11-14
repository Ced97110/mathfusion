"""Convert the machine learning book (PDF) into site pages. Zero tokens: pure script.

Usage (from the repo root):
    python3 tools/ml/build.py <book.pdf> [work_dir]
    ML_ONLY=002,003 python3 tools/ml/build.py ...   # rebuild some chapters only (keys)
    ML_RESUME=1 python3 tools/ml/build.py ...       # finish an interrupted run

Writes:
    content/ml.json               parts and chapters (table of contents)
    public/ml/cNNN.html           one HTML fragment per chapter
    public/ml/img/cNNN/*.svg      formulas, tables, boxes and figures, cut out of the PDF

The book is bilingual: each French paragraph is followed by its English translation
(blue, behind a vertical rule). Plain text lines are reflowed as HTML, with the language
kept (class "en" for English). Anything else (display formulas, tables, figures, box
headers) is cut out of the PDF as a vector SVG band (PyMuPDF), so nothing of the book is rewritten.
Same method as tools/physique/build.py, tuned to this PDF (Inter body, 425 x 756 px pages).
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
ONLY = {k for k in os.environ.get('ML_ONLY', '').split(',') if k}
RESUME = os.environ.get('ML_RESUME') == '1'  # keep chapters already written
SCALE = 1.5  # pdftohtml pixels per PDF point (108 dpi)
PAGE_W = 425
FOOTER_TOP = 722  # page numbers sit below this line
PARA_GAP = 25
INK_LEVEL = 170
NEAR = 4  # px around a text line searched for drawing ink
RULE_MIN = 12  # a vertical ink run this tall and at most 3 px wide is a rule, not a drawing
EN_COLORS = {'#2c5f8a', '#2d5f8b'}
HEAD_COLOR = '#b5462d'
TEXT_LEFT = 23


@dataclass
class Item:
    top: int
    left: int
    w: int
    h: int
    kind: str  # body | math | head | fig
    size: int
    en: bool
    bold_italic: bool
    lost: bool  # colour reported as pure black: pdftohtml lost it (top of a page)
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

    @property
    def en(self) -> bool:
        words = [i for i in self.items if i.kind == 'body'] or self.items
        return sum(i.en for i in words) * 2 > len(words)

    def plain(self) -> bool:
        """One baseline: body text at body size, inline math (subscripts allowed)."""
        for i in self.items:
            if i.kind == 'body' and not 13 <= i.size <= 16:
                return False
            if i.kind == 'math' and not 9 <= i.size <= 17:
                return False
            if i.kind in ('head', 'fig'):
                return False
        for a, b in zip(self.items, self.items[1:]):
            if b.left - (a.left + a.w) > 24:
                return False  # table row: cells far apart
        body = [i for i in self.items if i.kind == 'body'] or self.items
        tops = [i.top for i in body]
        return max(tops) - min(tops) <= 3 and self.bottom - self.top <= 26


@dataclass
class Block:
    kind: str  # p | h2 | cap | vis
    page: int
    top: int
    bottom: int
    lines: list[Line] = field(default_factory=list)
    left: int = 0
    right: int = 0
    en: bool = False
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


def outline(root: ET.Element) -> tuple[list[dict], list[dict]]:
    """Front texts (level 1 without children), parts (level 1) and chapters (level 2)."""
    kids = list(root.find('outline'))
    front, parts = [], []
    for i, el in enumerate(kids):
        if el.tag != 'item':
            continue
        title = clean_title(el.text or '')
        nxt = kids[i + 1] if i + 1 < len(kids) else None
        if nxt is None or nxt.tag != 'outline':
            front.append({'title': title, 'page': int(el.get('page'))})
            continue
        m = re.match(r'([IVXL]+) (.*)', title)
        chapters = []
        for c in nxt:
            if c.tag != 'item':
                continue
            ct = clean_title(c.text or '')
            cm = re.match(r'(\d+) (.*)', ct)
            chapters.append({'key': cm.group(1) if cm else slug(ct), 'title': cm.group(2) if cm else ct,
                             'page': int(c.get('page'))})
        parts.append({'num': m.group(1) if m else '', 'title': m.group(2) if m else title,
                      'page': int(el.get('page')), 'chapters': chapters})
    return front, parts


def part_english(pdf: str, page: int) -> str:
    """English title of a part: the blue text of its opening page."""
    out = subprocess.run(['pdftohtml', '-xml', '-i', '-q', '-stdout', '-f', str(page), '-l', str(page), pdf],
                         check=True, capture_output=True, text=True).stdout
    root = ET.fromstring(re.sub(r'<!DOCTYPE[^>]*>', '', out))
    blue = {fs.get('id') for fs in root.iter('fontspec') if fs.get('color') in EN_COLORS}
    words = [''.join(t.itertext()) for t in root.iter('text') if t.get('font') in blue]
    return clean_title(' '.join(words))


def kind_of(family: str, size: int, color: str) -> str:
    if 'DejaVu' in family:
        return 'fig'
    if 'LatinModernMath' in family:
        return 'math'
    if 'ExtraBold' in family and size >= 17:
        return 'head'
    return 'body'


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
        size, fam, color = fonts[t.get('font')]
        items.append(Item(top, int(t.get('left')), int(t.get('width')), int(t.get('height')),
                          kind_of(fam, size, color), size, color in EN_COLORS,
                          'BoldItalic' in fam, color == '#000000', inner))
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


def drop_rules(ink: np.ndarray) -> np.ndarray:
    """Remove thin vertical rules (the bar before English text, box edges)."""
    h, w = ink.shape
    out = ink.copy()
    for x in range(w):
        col = ink[:, x]
        if col.sum() < RULE_MIN:
            continue
        for a, b in runs(col):
            if b - a < RULE_MIN:
                continue
            # thin: 4 px further left and right there is (almost) no ink on these rows
            left = ink[a:b, x - 4].mean() if x >= 4 else 0.0
            right = ink[a:b, x + 4].mean() if x + 4 < w else 0.0
            if left < 0.5 and right < 0.5:
                out[a:b, x] = False
    return out


def ink_rows(raster: np.ndarray, items: list[Item]) -> np.ndarray:
    """Rows holding ink outside every text box (rules, frames, figures, tables)."""
    ink = drop_rules(raster < INK_LEVEL)
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


def ruled(raster: np.ndarray, ln: Line) -> bool:
    """English paragraphs sit behind a vertical rule at x 22-26. pdftohtml loses their blue
    colour at the top of a page (it reports pure black), so there the rule decides.
    Boxes also have a left edge, but their text keeps its colour."""
    words = [i for i in ln.items if i.kind == 'body']
    if not 30 <= ln.left <= 40 or not words or sum(i.lost for i in words) * 2 <= len(words):
        return False
    rows = raster[ln.top:ln.bottom, 21:28] < INK_LEVEL
    white = raster[ln.top:ln.bottom, 28:32].mean() > 248  # a box has a tinted fill there
    return bool(rows.any(axis=1).mean() > 0.6 and white)


def text_of(ln: Line) -> str:
    return re.sub('<[^>]+>', '', ''.join(i.text for i in ln.items)).strip()


def page_blocks(pn: int, items: list[Item], raster: np.ndarray) -> list[Block]:
    lines = group_lines(items)
    rows = ink_rows(raster, items)
    blocks: list[Block] = []
    for a, b in runs(rows):
        if b - a < 3:
            continue  # a lone horizontal rule (box edge) carries nothing
        cols = np.where((raster[a:b] < INK_LEVEL).any(axis=0))[0]
        blocks.append(Block('vis', pn, a, b, left=int(cols.min()), right=int(cols.max()) + 1))
    stacked = set()
    for a, b in zip(lines, lines[1:]):
        if b.top < a.bottom - 3:
            stacked |= {id(a), id(b)}
    for ln in lines:
        txt = text_of(ln)
        hits = rows[max(0, ln.top - NEAR):ln.bottom + NEAR].any()
        if all(i.kind == 'head' for i in ln.items) or all(i.bold_italic for i in ln.items):
            kind = 'h2'
        elif ln.plain() and not hits and id(ln) not in stacked:
            kind = 'cap' if re.match(r'F[Ii]ɢ\. ', txt) else 'p'
        else:
            kind = 'vis'
        blocks.append(Block(kind, pn, ln.top, ln.bottom, [ln], ln.left, ln.right, ln.en or ruled(raster, ln)))
    blocks.sort(key=lambda b: (b.top, b.kind != 'vis'))
    return merge(blocks)


def merge(blocks: list[Block]) -> list[Block]:
    """Join visual pieces that touch, and text lines into paragraphs of one language."""
    out: list[Block] = []
    for b in blocks:
        prev = out[-1] if out else None
        if prev and prev.kind == 'vis' and b.kind == 'vis' and b.top - prev.bottom < 28:
            absorb(prev, b)
        elif prev and prev.kind == 'vis' and b.top < prev.bottom:
            absorb(prev, b)
        elif prev and prev.kind in ('p', 'cap') and b.kind == 'p' and continues(prev, b):
            absorb(prev, b)
        elif prev and prev.kind == 'cap' and b.kind == 'p' and b.en and b.top - prev.bottom < 28:
            b.kind = 'cap'  # English half of a figure caption
            out.append(b)
        elif prev and prev.kind == 'h2' and b.kind == 'h2' and b.en and not prev.en:
            b.kind = 'h2en'
            out.append(b)
        else:
            out.append(b)
    return out


def absorb(a: Block, b: Block) -> None:
    a.top, a.bottom = min(a.top, b.top), max(a.bottom, b.bottom)
    a.left, a.right = min(a.left, b.left), max(a.right, b.right)
    a.lines += b.lines


def continues(prev: Block, b: Block) -> bool:
    if b.en != prev.en or b.top - prev.bottom > PARA_GAP - 14:
        return False
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
    """Keep 3 decimals (glyphs are in em units, page items in pt) and drop the data-text
    attributes: about a third lighter, no visible change."""
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


def pending_continues(pending: list[str], pending_en: bool, b: Block) -> bool:
    """A paragraph goes on across a page break unless the previous text ended a sentence."""
    if not b.page_start or b.en != pending_en:
        return False
    last = re.sub('<[^>]+>', '', pending[-1]).rstrip()
    return not re.search(r'[.?!:»”]$', last)


def chapter_html(blocks: list[Block], key: str, pdf: str, outdir: str, vocab: set[str]) -> str:
    imgdir = f'{outdir}/img/c{key}'
    shutil.rmtree(imgdir, ignore_errors=True)
    os.makedirs(imgdir)
    parts: list[str] = []
    pending: list[str] = []
    state = {'en': False, 'k': 0}

    def flush() -> None:
        if pending:
            cls = ' class="en"' if state['en'] else ''
            parts.append(f'<p{cls}>{join_lines(pending, vocab)}</p>')
            pending.clear()

    for b in blocks:
        if b.kind == 'p':
            if pending and not pending_continues(pending, state['en'], b):
                flush()
            state['en'] = b.en
            pending.extend(line_html(ln) for ln in b.lines)
            continue
        flush()
        if b.kind in ('h2', 'h2en'):
            head = re.sub(r'</?[bi]>', '', ' '.join(line_html(l) for l in b.lines))
            parts.append(f'<p class="h2en">{head}</p>' if b.kind == 'h2en' else f'<h2>{head}</h2>')
        elif b.kind == 'cap':
            cls = 'cap en' if b.en else 'cap'
            parts.append(f'<p class="{cls}">{join_lines([line_html(l) for l in b.lines], vocab)}</p>')
        else:
            state['k'] += 1
            x0, x1 = max(0, min(b.left, TEXT_LEFT) - 5), min(PAGE_W, max(b.right, 402) + 5)
            y0, y1 = max(0, b.top - 3), min(FOOTER_TOP, b.bottom + 3)
            name = f'p{b.page:04d}_{state["k"]}.svg'
            svg_band(pdf, b.page, x0, y0, x1 - x0, y1 - y0, f'{imgdir}/{name}')
            alt = html.escape(' '.join(re.sub('<[^>]+>', '', line_html(l)) for l in b.lines), quote=True)
            fig = any(i.kind == 'fig' for l in b.lines for i in l.items) or not b.lines
            parts.append(f'<img class="{"vf" if fig else "vm"}" src="/ml/img/c{key}/{name}" alt="{alt}" '
                         f'style="--w:{(x1 - x0) / 16:.2f}" loading="lazy">')
    flush()
    return '\n'.join(parts)


def first_page_title(blocks: list[Block]) -> tuple[list[Block], str]:
    """Drop the chapter heading (label, title, English title) at the top; return the English title."""
    out = list(blocks)
    en_title = ''
    while out and out[0].page == blocks[0].page:
        b = out[0]
        txt = ' '.join(text_of(l) for l in b.lines)
        if b.kind == 'h2' and re.match(r'Chapitre \d+$', txt):
            out.pop(0)
        elif b.kind in ('h2', 'vis') and b.top < 200 and not txt.startswith('Sources'):
            # title (24 px) and English title (17 px blue) come out as heading or visual lines
            if any(i.en for l in b.lines for i in l.items):
                en_title = txt
            out.pop(0)
        else:
            break
    return out, en_title


def rasters(pdf: str, first: int, last: int, tmp: str) -> dict[int, np.ndarray]:
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    run(['pdftoppm', '-r', '108', '-gray', '-f', str(first), '-l', str(last), pdf, f'{tmp}/p'])
    out = {}
    for f in os.listdir(tmp):
        out[int(re.search(r'(\d+)\.pgm$', f).group(1))] = np.asarray(Image.open(os.path.join(tmp, f)))
    return out


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = os.path.abspath(sys.argv[1])
    work = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else f'{ROOT}/book/ml-work')
    root = load_xml(pdf, work)
    front, parts = outline(root)
    pages = {int(p.get('number')): p for p in root.iter('page')}
    fonts: dict = {}
    for p in pages.values():
        for fs in p.iter('fontspec'):
            fonts[fs.get('id')] = (int(fs.get('size')), fs.get('family'), fs.get('color'))
    vocab = vocabulary(root)
    outdir = f'{ROOT}/public/ml'
    os.makedirs(outdir, exist_ok=True)
    starts = sorted({f['page'] for f in front} | {p['page'] for p in parts}
                    | {c['page'] for p in parts for c in p['chapters']})
    tmp = tempfile.mkdtemp(prefix='ml-ras-')

    def blocks_of(first: int) -> list[Block]:
        later = [s for s in starts if s > first]
        last = (later[0] - 1) if later else max(pages)
        ras = rasters(pdf, first, last, tmp)
        out: list[Block] = []
        for pn in range(first, last + 1):
            bl = page_blocks(pn, page_items(pages[pn], fonts), ras[pn])
            if bl:
                bl[0].page_start = True
            out += bl
        return out

    def write(key: str, label: str, title: str, page: int) -> dict:
        if RESUME and os.path.exists(f'{outdir}/c{key}.html'):
            return {'key': key, 'title': title, 'file': f'c{key}.html'}
        bl, en_title = first_page_title(blocks_of(page))
        body = chapter_html(bl, key, pdf, outdir, vocab)
        head = f'<div class="pk">{label}</div>\n' if label else ''
        sub = f'\n<p class="h1en">{en_title}</p>' if en_title else ''
        with open(f'{outdir}/c{key}.html', 'w', encoding='utf8') as fh:
            fh.write(f'{head}<h1>{html.escape(title)}</h1>{sub}\n{body}')
        print(f'{key:>8}  p.{page:<5} {title[:60]}', flush=True)
        return {'key': key, 'title': title, 'en': en_title, 'file': f'c{key}.html'}

    toc: dict = {'front': [], 'parts': []}
    try:
        for i, f in enumerate(front):
            key = f'0{i + 1}'
            entry = {'key': key, 'title': f['title'], 'file': f'c{key}.html'}
            if not ONLY or key in ONLY:
                entry = write(key, '', f['title'], f['page'])
            toc['front'].append(entry)
        for p in parts:
            entry = {'num': p['num'], 'title': p['title'], 'en': part_english(pdf, p['page']), 'chapters': []}
            for c in p['chapters']:
                key = c['key'] if not c['key'].isdigit() else f'{int(c["key"]):03d}'
                label = f'Chapitre {int(c["key"])}' if c['key'].isdigit() else ''
                ch = {'key': key, 'title': c['title'], 'file': f'c{key}.html'}
                if not ONLY or key in ONLY or c['key'] in ONLY:
                    ch = write(key, label, c['title'], c['page'])
                entry['chapters'].append(ch)
            toc['parts'].append(entry)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if not ONLY:
        with open(f'{ROOT}/content/ml.json', 'w', encoding='utf8') as fh:
            json.dump(toc, fh, ensure_ascii=False, indent=1)
    print('ml :', sum(len(p['chapters']) for p in toc['parts']), 'chapitres')


def slug(title: str) -> str:
    import unicodedata
    t = unicodedata.normalize('NFD', title.lower()).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


if __name__ == '__main__':
    main()
