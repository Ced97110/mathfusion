import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(58)
text(ax, 22, 52, r'forme : $P^T A P$', 'sujet', 's'); text(ax, 66, 52, r'transformation : $P^{-1} A P$', 'autre', 's')
box(ax, 3, 6, 39, 40, 'sujet', fill=False, lw=0.6); box(ax, 46, 6, 39, 40, 'autre', fill=False, lw=0.6)
mat(ax, 22, 28, [['1', '1'], ['1', '−1']], 'sujet', dx=8, dy=8, size='l')
mat(ax, 66, 28, [['½', '½'], ['½', '−½']], 'autre', dx=8, dy=8, size='l')
text(ax, 22, 12, r'$P^T$', 'sujet', 'm'); text(ax, 66, 12, r'$P^{-1}$', 'autre', 'm')
text(ax, 44, 28, r'$\neq$', 'limite', 'xl')
save(fig, '71-064')
