import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 7.0; o = (8.0, 10.0)
P = lambda a, b: (o[0] + a * u, o[1] + b * u)
poly(ax, [P(0, 0), P(2, 1), P(3, 4), P(1, 3)], 'resultat')
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.3); arrow(ax, P(0, 0), P(1, 3), 'varie', lw=1.3)
text(ax, P(2, 1)[0] + 7, P(2, 1)[1] - 2, r'$Te_1$', 'sujet', 'm'); text(ax, P(1, 3)[0] - 5, P(1, 3)[1] + 1, r'$Te_2$', 'varie', 'm')
text(ax, 15, 4, 'carré unité : gris', 'fixe', 's')
text(ax, 54, 58, r'$Te_1$', 'sujet', 'm'); text(ax, 68, 58, r'$Te_2$', 'varie', 'm')
vals = [[2, 1], [1, 3]]
for r in range(2):
    for c in range(2):
        role = 'sujet' if c == 0 else 'varie'
        box(ax, 47 + 14 * c, 40 - 11 * r, 14, 11, role, label=str(vals[r][c]), size='l')
for x, sg in ((45.5, 1.5), (76.5, -1.5)):
    line(ax, [(x + sg, 52), (x, 52), (x, 29), (x + sg, 29)], 'encre')
box(ax, 44, 17, 42, 10, 'fixe', label=r'$2\times3-1\times1$')
arrow(ax, (65, 16.5), (65, 13), 'fixe')
box(ax, 44, 1.5, 42, 11, 'resultat', label=r'$\det T=5$', size='l', weight='bold')
save(fig, '76-103')
