import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
OX, OY, U = 14, 8, 10.0
P = lambda x, y: (OX + x * U, OY + y * U)
line(ax, [P(0, 0), P(6, 0)], 'fixe'); line(ax, [P(0, 0), P(0, 6)], 'fixe')
for v in range(1, 7):
    line(ax, [P(v, -0.12), P(v, 0.12)], 'fixe', lw=0.6); line(ax, [P(-0.12, v), P(0.12, v)], 'fixe', lw=0.6)
for v in (0, 2, 4, 6): text(ax, P(v, 0)[0], OY - 3.5, str(v), 'fixe', 's')
for v in (2, 4, 6): text(ax, OX - 3.5, P(0, v)[1], str(v), 'fixe', 's')
text(ax, P(6.3, 0)[0], OY - 3.5, r'$x$', 'fixe', 's'); text(ax, OX - 3.5, P(0, 6.5)[1], r'$y$', 'fixe', 's')
line(ax, [P(0, 5), P(5, 0)], 'sujet', lw=1.2)
line(ax, [P(1, 6), P(4, 0)], 'autre', lw=1.2)
text(ax, *P(5.45, 0.55), r'$D_1$', 'sujet', 'm'); text(ax, *P(0.4, 6.35), r'$D_2$', 'autre', 'm')
line(ax, [P(4, 1), P(4, 0)], 'varie', dash=True, lw=0.9)
disc(ax, *P(4, 0), 1.2, 'autre'); disc(ax, *P(4, 1), 1.5, 'varie')
text(ax, *P(4.9, 1.2), r'$(4,\,1)$', 'varie', 's'); text(ax, *P(3.5, -0.0 + 0.55), r'$(4,\,0)$', 'autre', 's') if False else None
text(ax, *P(4.9, 0.0 + 2.3), 'sur $D_1$,\nhors de $D_2$', 'encre', 's')
save(fig, '24-023')
