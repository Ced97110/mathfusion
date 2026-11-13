import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(56)
u = 14; o = (8, 12)
arrow(ax, o, (o[0] + u, o[1]), 'sujet', lw=1.6)
arrow(ax, o, (o[0], o[1] + u), 'autre', lw=1.6)
text(ax, o[0] + u / 2, o[1] - 4, r'$e_1$', 'sujet', 'm'); text(ax, o[0] - 4, o[1] + u / 2, r'$e_2$', 'autre', 'm')
text(ax, 44, 48, 'produit scalaire', 'encre', 's', ha='right')
vals = [[1, 0], [0, 1]]
for i in range(2):
    for j in range(2):
        r = 'resultat' if vals[i][j] else 'fixe'
        box(ax, 36 + j * 25, 24 - i * 12, 24, 11, r, label=r'$b_{%d%d} = %d$' % (i + 1, j + 1, vals[i][j]), size='s')
text(ax, 60, 8, 'matrice unité', 'resultat', 'm')
save(fig, '71-060')
