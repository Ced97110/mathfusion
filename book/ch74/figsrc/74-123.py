import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 9; ox = 26; oy = 30
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(-2, 3):
    for j in range(-2, 3):
        disc(ax, *P(i, j), 0.7, 'fixe')
arrow(ax, P(0, 0), P(0.88, 0), 'sujet', lw=1.4); arrow(ax, P(0, 0), P(0, 0.88), 'autre', lw=1.4)
disc(ax, *P(1, 0), 1.0, 'sujet'); disc(ax, *P(0, 1), 1.0, 'autre'); disc(ax, *P(-1, 0), 1.0, 'resultat')
arrow(ax, P(1.1, 0.15), P(0.15, 1.1), 'varie', lw=1.2, curve=0.4)
arrow(ax, P(-0.15, 1.1), P(-1.1, 0.15), 'varie', lw=1.2, curve=0.4)
text(ax, *P(1.0, -0.5), r'$x$', 'sujet', 'm'); text(ax, *P(-0.4, 0.7), r'$y$', 'autre', 'm')
text(ax, *P(1.55, 1.55), 'quart de tour', 'varie', 's')
box(ax, 52, 36, 34, 9, 'sujet', label=r'$Rx=0\,x+1\,y$', size='s')
box(ax, 52, 24, 34, 9, 'autre', label=r'$Ry=-1\,x+0\,y$', size='s')
text(ax, 69, 14, '4 coefficients entiers', 'resultat', 's')
save(fig, '74-123')
