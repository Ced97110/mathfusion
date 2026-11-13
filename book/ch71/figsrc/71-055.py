import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(72)
u = 6; o = (12, 8)
P = lambda a, b: (o[0] + a * u, o[1] + b * u)
arrow(ax, P(0, 0), P(4, 8), 'varie', lw=1.2)
for k in range(1, 4):
    a, b = P(k, 2 * k)
    line(ax, [(a - 1.4, b + 0.7), (a + 1.4, b - 0.7)], 'varie', lw=0.9)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.6)
arrow(ax, P(0, 0), P(3, 1), 'fixe', lw=1.2)
text(ax, P(3, 1)[0] + 2, P(3, 1)[1] - 3, r'$x = (3\,;\,1)$ fixé', 'fixe', 's', ha='left')
text(ax, P(1, 2)[0] - 2, P(1, 2)[1] + 2, r'$y = (1\,;\,2)$', 'autre', 's', ha='right')
text(ax, P(4, 8)[0] + 3, P(4, 8)[1] - 2, r'$4y = (4\,;\,8)$', 'varie', 's', ha='left')
text(ax, 62, 30, r'$B(x, y) = 5$', 'autre', 's')
text(ax, 62, 22, r'$B(x, 4y) = 20$', 'resultat', 's')
text(ax, 62, 14, r'$20 = 4 \times 5$', 'resultat', 's')
save(fig, '71-055')
