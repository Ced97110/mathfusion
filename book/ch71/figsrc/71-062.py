import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(60)
text(ax, 18, 52, r'$A$', 'sujet', 'l'); text(ax, 70, 52, r"$A' $", 'autre', 'l')
mat(ax, 18, 40, [['2   0'], ['0   1']], 'sujet', dx=13, dy=7)
mat(ax, 70, 40, [['3   1'], ['1   3']], 'autre', dx=13, dy=7)
arrow(ax, (33, 40), (55, 40), 'varie', lw=1.4)
text(ax, 44, 45, r'$P^T A P$', 'varie', 's')
text(ax, 18, 26, r'$x=(3\,;\,1),\ y=(1\,;\,1)$', 'sujet', 's')
text(ax, 70, 26, r"$x'=(2\,;\,1),\ y'=(1\,;\,0)$", 'autre', 's')
text(ax, 18, 14, r'$B = 7$', 'resultat', 'l'); text(ax, 70, 14, r'$B = 7$', 'resultat', 'l')
text(ax, 44, 14, '=', 'resultat', 'xl')
save(fig, '71-062')
