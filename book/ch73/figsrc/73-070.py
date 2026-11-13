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
fig, ax = canvas(46)
A = [[2, 0, 1], [0, 3, 4], [5, 0, 6]]; T = [[2, 0, 5], [0, 3, 0], [1, 4, 6]]
pitch = 7
xa, ya, cell = mat(ax, 20, 20, A, size='l', pitch=pitch)
xt, yt, _ = mat(ax, 68, 20, T, size='l', pitch=pitch)
for k in range(1, 3):
    cellbox(ax, xa[k], ya[k], cell, pitch, 'fixe'); cellbox(ax, xt[k], yt[k], cell, pitch, 'fixe')
for k in range(3):
    cellbox(ax, xa[k], ya[0], cell, pitch, 'varie'); cellbox(ax, xt[0], yt[k], cell, pitch, 'varie')
text(ax, 20, 38, r'$A$', 'sujet', 'l'); text(ax, 68, 38, r'$A^{t}$', 'sujet', 'l')
arrow(ax, (37, ya[0]), (50, ya[0]), 'varie')
text(ax, 43.5, ya[0] + 4, 'ligne 1', 'varie', 's'); text(ax, 43.5, ya[0] - 4, 'colonne 1', 'varie', 's')
text(ax, 44, 4, 'diagonale (gris) : ne bouge pas', 'fixe', 's')
save(fig, '73-070')
