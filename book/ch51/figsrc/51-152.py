import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

FS = ' '  # figure space: same width as a digit

def mat(ax, cx, cy, rows, role='sujet', size='m', n=2, sep=2, ls=2.2, col_roles=None, d=1):
    """Matrix drawn as aligned text with brackets. Returns (cell(i, j) -> (x, y), (x0, x1, y0, y1))."""
    fs = SIZE[size] * 25.4 / 72
    cw = 0.636 * fs
    px = (n + sep) * cw
    py = 1.05 * fs * (0.767 * ls + 0.194)
    nr, nc = len(rows), len(rows[0])
    cell = lambda i, j: (cx + (j - (nc - 1) / 2) * px, cy + ((nr - 1) / 2 - i) * py)
    fmt = lambda v: str(v).replace('-', '−').rjust(n, FS)
    if col_roles is None:
        t = text(ax, cx - (n - d) * cw / 2, cy, '\n'.join((FS * sep).join(fmt(v) for v in r) for r in rows), role, size)
        t.set_linespacing(ls)
    else:
        for j in range(nc):
            t = text(ax, cell(0, j)[0] - (n - d) * cw / 2, cy, '\n'.join(fmt(r[j]) for r in rows), col_roles[j], size)
            t.set_linespacing(ls)
    w = (nc - 1) * px + n * cw + 2.4
    h = nr * py + 0.6
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    for xs, d in ((x0, 1.2), (x1, -1.2)):
        line(ax, [(xs + d, y1), (xs, y1), (xs, y0), (xs + d, y0)], role, lw=0.9)
    return cell, (x0, x1, y0, y1)

def hl(ax, x0, x1, y0, y1, role='varie'):
    """Dashed highlight frame."""
    box(ax, x0, y0, x1 - x0, y1 - y0, role, fill=False, lw=1.0, r=0.6, dash=True)

fig, ax = canvas(52)
text(ax, 44, 48, r'on lit $S\,R\,u$, on applique de droite à gauche', 'fixe', 's')
bw, bh, by = 22, 11, 22
xs = (2, 33, 64)
box(ax, xs[0], by, bw, bh, 'sujet', label=r'$S$', size='l')
box(ax, xs[1], by, bw, bh, 'autre', label=r'$R$', size='l')
box(ax, xs[2], by, bw, bh, 'fixe', label=r'$u$', size='l')
top = by + bh + 1
arrow(ax, (xs[2] + bw / 2, top), (xs[1] + bw / 2 + 1, top), 'varie', curve=0.5, lw=1.1)
arrow(ax, (xs[1] + bw / 2, top), (xs[0] + bw / 2 + 1, top), 'varie', curve=0.5, lw=1.1)
text(ax, xs[1] + bw + 5.5 - 0.5, top + 9.5, 'd’abord', 'varie', 's')
text(ax, xs[0] + bw + 5.5 - 0.5, top + 9.5, 'ensuite', 'varie', 's')
text(ax, xs[2] + bw / 2, by - 5, r'$(1{,}5\ ;\ 0{,}5)$', 'fixe', 's')
text(ax, xs[1] + bw / 2, by - 5, r'$(-0{,}5\ ;\ 1{,}5)$', 'autre', 's')
text(ax, xs[0] + bw / 2, by - 5, r'$(-1\ ;\ 1{,}5)$', 'resultat', 's')
text(ax, xs[2] + bw / 2, by - 10.5, 'départ', 'fixe', 's')
text(ax, xs[1] + bw / 2, by - 10.5, 'après R', 'autre', 's')
text(ax, xs[0] + bw / 2, by - 10.5, 'après S', 'resultat', 's')
save(fig, '51-152')
