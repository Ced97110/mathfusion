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

fig, ax = canvas(56)
u = 18.0; ox, oy = 6.0, 14.0
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, (ox - 3, oy), (ox + 2 * u + 6, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 3), (ox, oy + u + 8), 'fixe', lw=0.6)
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'fixe')
poly(ax, [P(0, 0), P(2, 0), P(2, 1), P(0, 1)], 'sujet', fill=False, lw=1.3)
arrow(ax, (P(1, 0.5)[0] + 1, P(1, 0.5)[1]), (P(2, 0.5)[0] - 0.5, P(2, 0.5)[1]), 'varie', lw=1.3)
text(ax, P(0.5, 0.5)[0], P(0.5, 0.5)[1], 'carré', 'fixe', 's')
text(ax, P(1.5, 0.5)[0], P(1.5, 0.5)[1] + 3.6, '× 2', 'varie', 'm')
text(ax, P(1, 1)[0], P(1, 1)[1] + 5, 'hauteur inchangée', 'fixe', 's')
text(ax, P(1, 0)[0], P(1, 0)[1] - 4.5, 'largeur : 1 devient 2', 'sujet', 's')
text(ax, 65.5, 30, r'$S=$', 'sujet', 'm', ha='right')
mat(ax, 74, 30, [[2, 0], [0, 1]], 'fixe', col_roles=('varie', 'fixe'))
text(ax, 74, 17, 'x double, y reste', 'sujet', 's')
save(fig, '51-155')
