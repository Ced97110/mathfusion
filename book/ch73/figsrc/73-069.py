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
fig, ax = canvas(62)
text(ax, 14, 56, r'$A$', 'sujet', 'm'); text(ax, 38, 56, r'$A^{-1}$', 'varie', 'm'); text(ax, 72, 56, r'$A^{t}$', 'autre', 'm')
for y0, name, A, inv, tr, ok in [(36, 'quart de tour', [[0, -1], [1, 0]], [[0, 1], [-1, 0]], [[0, 1], [-1, 0]], True),
                                 (10, 'cisaillement', [[1, 1], [0, 1]], [[1, -1], [0, 1]], [[1, 0], [1, 1]], False)]:
    role = 'resultat' if ok else 'limite'
    text(ax, 14, y0 + 13, name, role, 's', weight='bold')
    mat(ax, 14, y0 + 4, A, 'sujet'); mat(ax, 38, y0 + 4, inv, 'varie')
    text(ax, 53, y0 + 4, '=' if ok else r'$\neq$', role, 'l', weight='bold')
    mat(ax, 72, y0 + 4, tr, 'autre')
save(fig, '73-069')
