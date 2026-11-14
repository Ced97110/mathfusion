import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(64)
u = 8; o = (26, 16)
P = lambda a, b: (o[0] + a * u, o[1] + b * u)
arrow(ax, (o[0] - 6, o[1]), (o[0] + 36, o[1]), 'fixe', lw=0.7); arrow(ax, (o[0], o[1] - 10), (o[0], o[1] + 32), 'fixe', lw=0.7)
arrow(ax, P(0, 0), P(1, 1), 'sujet', lw=1.6)
arrow(ax, P(0, 0), P(1, -1), 'autre', lw=1.6)
line(ax, [P(2, 2), P(3, 1)], 'autre', lw=1.6, dash=True)
arrow(ax, P(1, 1), P(2, 2), 'sujet', lw=1.6)
arrow(ax, P(2, 2), P(3, 1), 'autre', lw=1.6)
disc(ax, P(3, 1)[0], P(3, 1)[1], 1.1, 'resultat')
text(ax, P(0.5, 0.5)[0] - 2, P(0.5, 0.5)[1] + 2, r'$u_1$', 'sujet', 's', ha='right')
text(ax, P(1, -1)[0], P(1, -1)[1] - 4, r'$u_2$', 'autre', 's')
text(ax, P(1.5, 1.5)[0] - 2, P(1.5, 1.5)[1] + 3, r'$2u_1$', 'sujet', 's', ha='right')
text(ax, P(3, 1)[0] + 2, P(3, 1)[1] - 4, r'$x = (3\,;\,1)$', 'resultat', 's', ha='left')
text(ax, 7, 58, r"$x' = (2\,;\,1)$", 'encre', 's', ha='left')
text(ax, 6, 36, r'$P$', 'encre', 'm')
mat(ax, 14, 44, [['1', '1'], ['1', '−1']], dx=6, dy=6, roles=[['sujet', 'autre'], ['sujet', 'autre']])
text(ax, 14, 52, r'$u_1\ \ u_2$', 'fixe', 's')
save(fig, '71-061')
