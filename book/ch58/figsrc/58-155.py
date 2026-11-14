import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 6.0; ox, oy = 22.0, 16.0
P = lambda x, y: (ox + s * x, oy + s * y)
# le plan atteint par u et v : zone verte
poly(ax, [(2, 6), (44, 6), (44, 56), (2, 56)], 'resultat')
text(ax, 23, 52, 'tout le plan', 'resultat', 's')
arrow(ax, P(0, 0), P(3, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(1, 2), 'varie', lw=1.5)
arrow(ax, P(0, 0), P(-1, 3), 'autre', lw=1.5)
disc(ax, *P(0, 0), 0.7, 'encre')
text(ax, P(3, 1)[0] + 3, P(3, 1)[1] - 2, r'$u$', 'sujet', 'l')
text(ax, P(1, 2)[0] + 3, P(1, 2)[1] + 0.5, r'$v$', 'varie', 'l')
text(ax, P(-1, 3)[0] - 3, P(-1, 3)[1] + 0.5, r'$w$', 'autre', 'l')
# décompte : deux places, trois flèches
text(ax, 66, 54, '2 flèches suffisent', 'resultat', 's')
box(ax, 50, 40, 16, 8, 'sujet', label=r'$u$')
box(ax, 68, 40, 16, 8, 'varie', label=r'$v$')
box(ax, 59, 25, 16, 8, 'autre', dash=True, label=r'$w$')
arrow(ax, (58, 39), (62, 34), 'varie')
arrow(ax, (76, 39), (72, 34), 'varie')
text(ax, 67, 19, r'$w=-u+2v$', 'autre', 'm')
text(ax, 67, 11, '3 flèches : une de trop', 'fixe', 's')
save(fig, '58-155')
