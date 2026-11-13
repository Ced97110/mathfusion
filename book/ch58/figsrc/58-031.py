import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, k = 8, 8, 9.0
P = lambda a, b: (ox + a * k, oy + b * k)
# grille
for i in range(0, 7): line(ax, [P(i, 0), P(i, 5.3)], 'fixe', lw=0.25)
for j in range(0, 6): line(ax, [P(0, j), P(6.3, j)], 'fixe', lw=0.25)
# chemin 1 : axes (5 puis 4)
line(ax, [P(0, 0), P(5, 0), P(5, 4)], 'fixe', lw=1.4, dash=True)
# chemin 2 : 2u puis v
arrow(ax, P(0, 0), P(4, 2), 'autre', lw=1.4)
arrow(ax, P(4, 2), P(5, 4), 'autre', lw=1.4)
arrow(ax, P(0, 0), P(2, 1), 'autre', lw=1.4)
disc(ax, *P(5, 4), 1.6, 'sujet')
text(ax, P(5, 4)[0] - 4, P(5, 4)[1] + 3.5, r'$w$', 'sujet', 'l', weight='bold')
text(ax, P(5, 0)[0] + 1.2, P(5, 2)[1] - 3, '4', 'fixe', 'm', ha='left')
text(ax, P(2.5, 0)[0], P(0, 0)[1] - 3, '5', 'fixe', 'm')
text(ax, P(1, 1)[0] + 2, P(1, 0.5)[1] + 4.5, r'$u$', 'autre', 'm')
text(ax, P(4.5, 3)[0] - 3.5, P(4.5, 3)[1] + 0.5, r'$v$', 'autre', 'm')
text(ax, P(3, 1.5)[0] - 1, P(3, 1.5)[1] + 3.5, r'$2\,u$', 'autre', 'm')
box(ax, 2, 62, 38, 9, 'fixe', label=r'axes $(e_1, e_2)$ : (5, 4)', size='s')
box(ax, 46, 62, 40, 9, 'autre', label=r'flèches $(u, v)$ : (2, 1)', size='s')
save(fig, '58-031')
