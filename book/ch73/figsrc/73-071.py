import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
FS = ' '
def mat(ax, cx, cy, rows, role='encre', size='m', pitch=4.6, gap=3):
    """Matrix as one text per row; returns (xs, ys) of cell centres and cell pitch."""
    cw = 0.636 * SIZE[size] * 25.4 / 72
    n = len(rows[0]); cell = (2 + gap) * cw; width = n * cell - gap * cw; left = cx - width / 2
    pad = lambda v: str(v).replace('-', '−').rjust(2, FS)
    ys = [cy + (len(rows) - 1) / 2 * pitch - i * pitch for i in range(len(rows))]
    xs = [left + j * cell + 1.3 * cw for j in range(n)]
    for y, r in zip(ys, rows): text(ax, cx, y, (FS * gap).join(pad(v) for v in r), role, size)
    xl, xr, yt, yb = left - 3.2, left + width + 3.2, ys[0] + pitch / 2, ys[-1] - pitch / 2
    line(ax, [(xl + 1, yt), (xl, yt), (xl, yb), (xl + 1, yb)], 'encre'); line(ax, [(xr - 1, yt), (xr, yt), (xr, yb), (xr - 1, yb)], 'encre')
    return xs, ys, cell
def cellbox(ax, x, y, w, h, role):
    box(ax, x - w / 2 + 0.3, y - h / 2 + 0.3, w - 0.6, h - 0.6, role, r=0.3, lw=0.6)
fig, ax = canvas(62)
ox, oy, u = 44, 24, 4.0
line(ax, [(8, oy), (82, oy)], 'fixe'); line(ax, [(ox, 22), (ox, 52)], 'fixe')
P = (ox + 3 * u, oy + 4 * u); Q = (ox - 4 * u, oy + 3 * u)
arrow(ax, P, Q, 'varie', curve=0.35, lw=1.2)
arrow(ax, Q, P, 'resultat', curve=0.35, lw=1.2)
disc(ax, P[0], P[1], 1.3, 'sujet'); disc(ax, Q[0], Q[1], 1.3, 'sujet')
text(ax, P[0] + 4, P[1] + 4, '(3, 4)', 'sujet', 's'); text(ax, Q[0] - 4, Q[1] + 5, r'$(-4,\,3)$', 'sujet', 's')
text(ax, 44, 55, r'$A$ : quart de tour', 'varie', 's'); text(ax, 44, 28.5, r'$A^{t}$ : on revient', 'resultat', 's')
text(ax, 28, 14, r'$A^{t}=$', 'resultat', 'm')
mat(ax, 52, 14, [[0, 1], [-1, 0]], 'resultat', pitch=5)
text(ax, 44, 3.5, 'sans calculer d’inverse', 'resultat', 's')
save(fig, '73-071')
