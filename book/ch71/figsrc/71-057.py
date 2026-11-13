import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(62)
text(ax, 10, 52, r'$x^T$', 'sujet', 'm'); text(ax, 40, 52, r'$A$', 'fixe', 'm'); text(ax, 72, 52, r'$y$', 'autre', 'm')
mat(ax, 10, 43, [['3   1']], 'sujet', dx=11, dy=6)
mat(ax, 40, 43, [['2   0'], ['0   1']], 'fixe', dx=11, dy=6)
mat(ax, 72, 43, [['1'], ['2']], 'autre', dx=7, dy=6)
arrow(ax, (72, 33), (72, 27), 'varie', lw=1.2)
text(ax, 80, 30, r'$A\,y$', 'varie', 's', ha='left')
mat(ax, 72, 20, [['2'], ['2']], 'varie', dx=7, dy=6)
mat(ax, 30, 20, [['3   1']], 'sujet', dx=11, dy=6)
text(ax, 51, 20, r'$\times$', 'encre', 'm')
text(ax, 44, 6, r'$3\times2 + 1\times2 = 8$', 'resultat', 'm')
save(fig, '71-057')
