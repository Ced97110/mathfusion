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

fig, ax = canvas(72)
text(ax, 44, 68, 'deux chemins, un seul point d’arrivée', 'fixe', 's')
bw, bh = 25, 10
box(ax, 1, 28, bw, bh, 'fixe', label=r'$u\ (1{,}5\ ;\ 0{,}5)$', size='s')
box(ax, 31.5, 50, bw, bh, 'autre', label=r'$(-0{,}5\ ;\ 1{,}5)$', size='s')
box(ax, 62, 28, bw, bh, 'resultat', label=r'$(-1\ ;\ 1{,}5)$', size='s')
arrow(ax, (1 + bw * 0.6, 28 + bh + 0.6), (31.5 - 0.6, 50 + bh / 2), 'autre', lw=1.1)
arrow(ax, (31.5 + bw + 0.6, 50 + bh / 2), (62 + bw * 0.4, 28 + bh + 0.6), 'sujet', lw=1.1)
text(ax, 12, 50, r'$R$', 'autre', 'l')
text(ax, 76, 50, r'$S$', 'sujet', 'l')
arrow(ax, (1 + bw + 0.6, 33), (62 - 0.6, 33), 'resultat', lw=1.5)
text(ax, 44, 36.5, r'$SR$ en une fois', 'resultat', 's')
text(ax, 44, 22, 'chemin du haut : R puis S', 'fixe', 's')
text(ax, 44, 14, 'chemin direct : le produit SR', 'resultat', 's')
text(ax, 44, 6, 'même point : le produit est le bon', 'resultat', 's')
save(fig, '51-158')
