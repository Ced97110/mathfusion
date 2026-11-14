import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(62)
f = numberline(ax, 7, 28, 32, 0, 4, arrow_right=True)
disc(ax, f(3), 32, 1.8, 'autre')
text(ax, 21, 57, 'graphe du nombre 3', 'autre', 'm'); text(ax, 21, 5, 'un seul point', 'autre', 's')
P = plane(ax, 62, 17, 10, 6, (-1.5, 2.3), (-1.3, 5.3))
for i in range(7):
    x = -1 + i * 0.5; disc(ax, *P(x, 2 * x + 1), 1.4, 'sujet')
text(ax, 66, 57, "graphe d'une équation", 'sujet', 'm'); text(ax, 66, 5, 'tous les points solutions', 'sujet', 's')
text(ax, P(0, 1)[0] + 2.5, P(0, 1)[1] - 3.2, '(0, 1)', 'sujet', 's', ha='left')
text(ax, P(1, 3)[0] + 2.5, P(1, 3)[1] - 3.2, '(1, 3)', 'sujet', 's', ha='left')
save(fig, '19-050')
