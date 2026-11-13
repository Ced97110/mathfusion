"""Convert the physics book (PDF) into site pages. Zero tokens: pure script.

Usage (from the repo root):
    python3 tools/physique/build.py <book.pdf> [work_dir]

Writes:
    content/physique.json            parts and chapters (table of contents)
    public/physique/cNNN.html        one HTML fragment per chapter
    public/physique/img/cNNN/*.svg   display formulas, boxes and figures, cut out of the PDF

How a page is split: plain text lines (body font, one baseline) are reflowed as HTML.
Anything else (display formulas, fractions, framed boxes, figures) is cut out of the PDF
as a vector SVG band, so nothing of the book is rewritten or redrawn.
Drawings are found on a 108 dpi raster (same scale as the pdftohtml coordinates):
ink that lies outside every text box belongs to a drawing.
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

import numpy as np
from PIL import Image

LIMIT = int(os.environ.get('PHYS_LIMIT', '9999'))  # build only the first N chapters (tests)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCALE = 1.5  # pdftohtml pixels per PDF point (108 dpi)
FOOTER_TOP = 715  # page numbers sit below this line
CROP_BOTTOM = 722  # lowest pixel a band may reach (the page number starts at 724)
PARA_GAP = 25  # vertical gap (px) above which a new paragraph starts
BODY_SIZES = range(14, 18)
INK_LEVEL = 170
NEAR = 5  # px around a text line searched for drawing ink  # gray level below which a raster pixel counts as ink


@dataclass
class Item:
    top: int
    left: int
    w: int
    h: int
    kind: str  # body | math | head | fig
    size: int
    text: str  # inner XML (already escaped, may hold <i>/<b>)

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
        """One baseline, body or inline-math glyphs at body size only."""
        if any(i.kind not in ('body', 'math') or i.size not in BODY_SIZES for i in self.items):
            return False
        tops = [i.top for i in self.items]
        return max(tops) - min(tops) <= 3 and max(i.h for i in self.items) <= 18


@dataclass
class Block:
    kind: str  # p | h2 | cap | vis
    page: int
    top: int
    bottom: int
    lines: list[Line] = field(default_factory=list)
    left: int = 0
    right: int = 0


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def prepare(pdf: str, work: str) -> None:
    """Cache the pdftohtml XML and the 108 dpi rasters."""
    os.makedirs(f'{work}/ras', exist_ok=True)
    if not os.path.exists(f'{work}/all.xml'):
        run(['pdftohtml', '-xml', '-i', '-q', pdf, f'{work}/all'])
    if not os.listdir(f'{work}/ras'):
        run(['pdftoppm', '-r', '108', '-gray', '-png', pdf, f'{work}/ras/p'])


def load_xml(work: str) -> ET.Element:
    src = open(f'{work}/all.xml', encoding='utf8').read()
    return ET.fromstring(re.sub(r'<!DOCTYPE[^>]*>', '', src))


def outline(root: ET.Element) -> list[dict]:
    """Parts (level 1) and chapters (level 2) from the PDF bookmarks."""
    top = root.find('outline')
    parts: list[dict] = []
    front: list[dict] = []
    kids = list(top)
    for i, el in enumerate(kids):
        if el.tag != 'item':
            continue
        title = el.text.strip().replace("'", '’')
        nxt = kids[i + 1] if i + 1 < len(kids) else None
        if nxt is not None and nxt.tag == 'outline':
            chapters = [
                {'title': c.text.strip().replace("'", '’'), 'page': int(c.get('page'))}
                for c in nxt if c.tag == 'item'
            ]
            parts.append({'title': title, 'page': int(el.get('page')), 'chapters': chapters})
        else:
            front.append({'title': title, 'page': int(el.get('page'))})
    return front, parts


def kind_of(family: str) -> str:
    if 'DejaVu' in family:
        return 'fig'
    if 'LatinModernMath' in family:
        return 'math'
    if 'LMSans' in family:
        return 'head'
    return 'body'


def page_items(page: ET.Element, fonts: dict) -> list[Item]:
    for fs in page.iter('fontspec'):
        fonts[fs.get('id')] = (int(fs.get('size')), fs.get('family'))
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
        items.append(Item(top, int(t.get('left')), int(t.get('width')), int(t.get('height')),
                          kind_of(fam), size, inner))
    return items


def group_lines(items: list[Item]) -> list[Line]:
    """Cluster items by vertical centre (same method as tools/kit/parse.py)."""
    def ctr(it: Item) -> float:
        return it.top + it.h / 2

    groups: list[list[Item]] = []
    for it in sorted(items, key=ctr):
        if groups and abs(ctr(it) - ctr(groups[-1][0])) <= 6:
            groups[-1].append(it)
        else:
            groups.append([it])
    return [Line(sorted(g, key=lambda i: i.left)) for g in groups]


def ink_rows(raster: np.ndarray, items: list[Item]) -> np.ndarray:
    """Rows holding ink outside every text box (rules, frames, figures)."""
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


def page_blocks(pn: int, items: list[Item], raster: np.ndarray) -> list[Block]:
    lines = group_lines(items)
    rows = ink_rows(raster, items)
    blocks: list[Block] = []
    for a, b in runs(rows):
        cols = np.where((raster[a:b] < INK_LEVEL).any(axis=0))[0]
        blocks.append(Block('vis', pn, a, b, left=int(cols.min()), right=int(cols.max()) + 1))
    # Lines that overlap a neighbour vertically are stacked math (fractions, limits).
    stacked = set()
    for a, b in zip(lines, lines[1:]):
        if b.top < a.bottom - 1:
            stacked |= {id(a), id(b)}
    for ln in lines:
        txt = re.sub('<[^>]+>', '', ''.join(i.text for i in ln.items)).strip()
        # rules just above or below (fraction bars) make the line part of a formula
        hits = rows[max(0, ln.top - NEAR):ln.bottom + NEAR].any()
        if all(i.kind == 'head' for i in ln.items):
            kind = 'h2'
        elif ln.plain() and not hits and id(ln) not in stacked:
            kind = 'cap' if re.match(r'Fig\. [0-9]', txt) else 'p'
        else:
            kind = 'vis'
        blocks.append(Block(kind, pn, ln.top, ln.bottom, [ln], ln.left, ln.right))
    blocks.sort(key=lambda b: (b.top, b.kind != 'vis'))
    return merge(blocks)


def merge(blocks: list[Block]) -> list[Block]:
    """Join visual pieces that touch, and text lines into paragraphs."""
    out: list[Block] = []
    for b in blocks:
        prev = out[-1] if out else None
        if prev and prev.kind == 'vis' and b.kind == 'vis' and b.top - prev.bottom < 14:
            absorb(prev, b)
        elif prev and prev.kind == 'vis' and b.top < prev.bottom:
            absorb(prev, b)  # a line inside a drawing belongs to it
        elif prev and prev.kind in ('p', 'cap') and b.kind == 'p' and continues(prev, b):
            absorb(prev, b)
        else:
            out.append(b)
    # A paragraph that holds a visual line (subscript, inline fraction) becomes one visual band,
    # so a sentence is never split between HTML text and an image. Display formulas and figures
    # (no body text in the band) stay apart from the text around them.
    changed = True
    while changed:
        changed = False
        for i in range(len(out) - 1):
            a, b = out[i], out[i + 1]
            pair = {a.kind, b.kind}
            if pair == {'vis', 'p'} and b.top - a.bottom <= 9:
                vis = a if a.kind == 'vis' else b
                if inline_text(vis):
                    absorb(a, b)
                    a.kind = 'vis'
                    del out[i + 1]
                    changed = True
                    break
    return out


def inline_text(b: Block) -> bool:
    """A visual band made of running text with math in it (not a figure, not a lone formula)."""
    items = [i for ln in b.lines for i in ln.items]
    return bool(items) and not any(i.kind == 'fig' for i in items) and any(i.kind == 'body' for i in items)


def absorb(a: Block, b: Block) -> None:
    a.top, a.bottom = min(a.top, b.top), max(a.bottom, b.bottom)
    a.left, a.right = min(a.left, b.left), max(a.right, b.right)
    a.lines += b.lines


def continues(prev: Block, b: Block) -> bool:
    if b.top - prev.bottom > PARA_GAP - 16:
        return False
    first = b.lines[0]
    return not (first.left > prev.lines[-1].left + 30)  # strong indent = new item


def line_html(ln: Line) -> str:
    out, prev = [], None
    for i in ln.items:
        if prev is not None and i.left - (prev.left + prev.w) >= 2:
            out.append(' ')  # a real gap on the page
        out.append(f'<span class="m">{i.text}</span>' if i.kind == 'math' else i.text)
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
            if joined in vocab or hyph not in vocab:
                text = text[:-1] + s
                continue
            text += s
            continue
        text += ' ' + s
    return re.sub(r'</i>\s*<i>', ' ', re.sub(r'</b>\s*<b>', ' ', text))


JOBS: list[tuple] = []  # SVG cuts, run in parallel at the end (pdftocairo is the slow part)


def svg_band(pdf: str, pn: int, x: int, y: int, w: int, h: int, dst: str) -> None:
    """Cut a band out of page pn as a vector SVG (coordinates in pdftohtml pixels)."""
    import math
    x0, y0 = math.floor(x / SCALE), math.floor(y / SCALE)
    pt = [x0, y0, math.ceil((x + w) / SCALE) - x0, math.ceil((y + h) / SCALE) - y0]
    run(['pdftocairo', '-svg', '-f', str(pn), '-l', str(pn), '-x', str(pt[0]), '-y', str(pt[1]),
         '-W', str(pt[2]), '-H', str(pt[3]), pdf, dst])
    src = open(dst, encoding='utf8').read()
    # Vector output keeps the page size and centres the crop area on the page.
    m = re.search(r'width="([0-9.]+)pt" height="([0-9.]+)pt" viewBox="[^"]+"', src)
    vx, vy = (float(m.group(1)) - pt[2]) / 2, (float(m.group(2)) - pt[3]) / 2
    src = src[:m.start()] + (f'width="{pt[2]}pt" height="{pt[3]}pt" '
                             f'viewBox="{vx:.3f} {vy:.3f} {pt[2]} {pt[3]}"') + src[m.end():]
    open(dst, 'w', encoding='utf8').write(shrink(src))


def shrink(src: str) -> str:
    """Round coordinates to 0.01 pt (invisible on screen) and drop blank lines: about half the size."""
    decl, _, src = src.partition('\n')  # keep <?xml version="1.0"?> untouched
    src = re.sub(r'(\d+\.\d{2})\d+', r'\1', src)
    src = re.sub(r'(\d)\.?0+(?=[ ,"])', lambda m: m.group(0) if '.' not in m.group(0) else m.group(1), src)
    return decl + '\n' + re.sub(r'\n\s*', '\n', src)


def vocabulary(root: ET.Element) -> set[str]:
    words: Counter = Counter()
    for t in root.iter('text'):
        for w in re.findall(r"[a-zà-ÿœ]+(?:-[a-zà-ÿœ]+)*", (''.join(t.itertext())).lower()):
            words[w] += 1
    return set(words)


def chapter_html(blocks: list[Block], key: str, pdf: str, outdir: str, vocab: set[str]) -> str:
    parts, k = [], 0
    pending: list[str] = []  # lines of the paragraph being built (may cross a page)

    def flush() -> None:
        if pending:
            parts.append(f'<p>{join_lines(pending, vocab)}</p>')
            pending.clear()

    for j, b in enumerate(blocks):
        if b.kind == 'p':
            if pending and not pending_continues(pending, b):
                flush()
            pending.extend(line_html(ln) for ln in b.lines)
            continue
        flush()
        if b.kind == 'h2':
            head = re.sub(r'</?b>', '', ' '.join(line_html(ln) for ln in b.lines))
            parts.append(f'<p class="src">{head}</p>' if head.startswith('Sources') else f'<h2>{head}</h2>')
        elif b.kind == 'cap':
            parts.append(f'<p class="cap">{join_lines([line_html(ln) for ln in b.lines], vocab)}</p>')
        else:
            k += 1
            x0, x1 = max(0, min(b.left, 26) - 6), min(425, max(b.right, 400) + 6)
            # pad by 4 px, but never reach into the text line just above or below
            above = blocks[j - 1].bottom + 1 if j and blocks[j - 1].page == b.page else 0
            below = blocks[j + 1].top - 1 if j + 1 < len(blocks) and blocks[j + 1].page == b.page else CROP_BOTTOM
            y0, y1 = max(above, b.top - 4), min(below, b.bottom + 4)
            name = f'p{b.page:04d}_{k}.svg'
            os.makedirs(f'{outdir}/img/c{key}', exist_ok=True)
            JOBS.append((pdf, b.page, x0, y0, x1 - x0, y1 - y0, f'{outdir}/img/c{key}/{name}'))
            alt = html.escape(' '.join(re.sub('<[^>]+>', '', line_html(ln)) for ln in b.lines), quote=True)
            fig = any(i.kind == 'fig' for ln in b.lines for i in ln.items) or not b.lines
            cls = 'vf' if fig else 'vm'
            parts.append(f'<img class="{cls}" src="/physique/img/c{key}/{name}" alt="{alt}" '
                         f'style="--w:{(x1 - x0) / 16:.2f}" loading="lazy">')
        b._continued = False
    flush()
    return '\n'.join(parts)


def pending_continues(pending: list[str], b: Block) -> bool:
    """A paragraph goes on across a page break unless the previous text ended a sentence."""
    if not getattr(b, 'page_start', False):
        return False
    last = re.sub('<[^>]+>', '', pending[-1]).rstrip()
    return not re.search(r'[.?!:»]$', last)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = os.path.abspath(sys.argv[1])
    work = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else f'{ROOT}/book/physique-work')
    prepare(pdf, work)
    root = load_xml(work)
    front, parts = outline(root)
    pages = {int(p.get('number')): p for p in root.iter('page')}
    vocab = vocabulary(root)
    outdir = f'{ROOT}/public/physique'
    os.makedirs(outdir, exist_ok=True)
    part_pages = {p['page'] for p in parts}
    starts = sorted([c['page'] for p in parts for c in p['chapters']] + [f['page'] for f in front] + list(part_pages))
    fonts: dict = {}
    for p in pages.values():
        for fs in p.iter('fontspec'):
            fonts[fs.get('id')] = (int(fs.get('size')), fs.get('family'))

    def blocks_of(first: int) -> list[Block]:
        later = [s for s in starts if s > first]
        last = (later[0] - 1) if later else max(pages)
        out: list[Block] = []
        for pn in range(first, last + 1):
            raster = np.asarray(Image.open(f'{work}/ras/p-{pn:04d}.png').convert('L'))
            bl = page_blocks(pn, page_items(pages[pn], fonts), raster)
            if bl:
                bl[0].page_start = True
            out += bl
        return out

    toc = {'front': [], 'parts': []}
    n = 0
    for i, f in enumerate(front):
        key = slug(f['title'])
        body = chapter_html(drop_title(blocks_of(f['page']), f['title']), key, pdf, outdir, vocab)
        open(f'{outdir}/c{key}.html', 'w', encoding='utf8').write(f'<h1>{f["title"]}</h1>\n{body}')
        toc['front'].append({'key': key, 'title': f['title'], 'file': f'c{key}.html'})
    for p in parts:
        entry = {'title': p['title'], 'chapters': []}
        for c in p['chapters']:
            n += 1
            if n > LIMIT:
                continue
            key = f'{n:03d}'
            bl = drop_title(blocks_of(c['page']), c['title'])
            body = chapter_html(bl, key, pdf, outdir, vocab)
            head = f'<div class="pk">Chapitre {n}</div>\n<h1>{c["title"]}</h1>'
            open(f'{outdir}/c{key}.html', 'w', encoding='utf8').write(f'{head}\n{body}')
            entry['chapters'].append({'key': str(n), 'title': c['title'], 'file': f'c{key}.html'})
            if n % 10 == 0:
                print(f'chapitre {n:3d}  p.{c["page"]}  {c["title"][:60]}', flush=True)
        toc['parts'].append(entry)
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
        list(pool.map(lambda job: svg_band(*job), JOBS))
    print(len(JOBS), 'bandes SVG')
    json.dump(toc, open(f'{ROOT}/content/physique.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('physique :', n, 'chapitres')


def slug(title: str) -> str:
    import unicodedata
    t = unicodedata.normalize('NFD', title.lower()).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def drop_title(blocks: list[Block], title: str) -> list[Block]:
    """Remove the chapter heading lines (number + title) at the top of the first page."""
    out = list(blocks)
    while out and out[0].kind == 'h2' and not re.match(r'[0-9] · ', strip(out[0])):
        out.pop(0)
    return out


def strip(b: Block) -> str:
    return re.sub('<[^>]+>', '', ' '.join(i.text for ln in b.lines for i in ln.items)).strip()


if __name__ == '__main__':
    main()
