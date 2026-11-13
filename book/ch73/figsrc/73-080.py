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
fig, ax = canvas(60)
pitch = 11
xs, ys, cell = mat(ax, 30, 28, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], size='xl', pitch=pitch, gap=3)
for i in range(3):
    for j in range(3):
        cellbox(ax, xs[j], ys[i], cell, pitch, 'resultat' if i == j else 'fixe')
text(ax, 30, 52, r'colonne $s$', 'encre', 's')
for k in range(3): text(ax, xs[k], 47, str(k + 1), 'encre', 's'); text(ax, xs[0] - 12, ys[k], str(k + 1), 'encre', 's')
text(ax, 4, 47, r'$r$', 'encre', 's', ha='left')
box(ax, 58, 38, 28, 10, 'resultat', label=r'$r=s$ : $1$', size='s')
box(ax, 58, 22, 28, 10, 'fixe', label=r'$r\neq s$ : $0$', size='s')
text(ax, 72, 14, r'$\delta_{rs}$ = case $(r,s)$', 'encre', 's'); text(ax, 72, 9.5, 'de l’identité', 'encre', 's')
save(fig, '73-080')
