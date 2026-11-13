import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 23, 34, 6.2
P = lambda a, b: (ox + a * u, oy + b * u)
# X + Y = tout le plan (zone grise), Z à l'intérieur
poly(ax, [P(-3, -3), P(3, -3), P(3, 3), P(-3, 3)], 'fixe')
text(ax, P(1.6, -2.5)[0], P(1.6, -2.5)[1], 'X + Y = plan', 'fixe', 's')
arrow(ax, P(-3, 0), P(3, 0), 'sujet', lw=1.2)
arrow(ax, P(0, -3), P(0, 3), 'autre', lw=1.2)
arrow(ax, P(-2.6, -2.6), P(2.6, 2.6), 'varie', lw=1.6)
text(ax, P(2.6, 0)[0], P(2.6, 0)[1] - 3, 'X', 'sujet', 's', weight='bold')
text(ax, P(0, 2.6)[0] + 3, P(0, 2.6)[1] - 4.2, 'Y', 'autre', 's', weight='bold')
text(ax, P(2.0, 2.7)[0], P(2.0, 2.7)[1], 'Z', 'varie', 's', weight='bold')
text(ax, 67, 56, 'Z face à…', 'encre', 's', weight='bold')
text(ax, 67, 47, r'$\checkmark\ Z\cap X=\{O\}$', 'resultat', 's')
text(ax, 67, 39, r'$\checkmark\ Z\cap Y=\{O\}$', 'resultat', 's')
box(ax, 48, 20, 38, 12, 'limite', label=r'$Z\cap(X+Y)=Z$', size='m', weight='bold')
text(ax, 67, 13, 'la somme contient Z', 'limite', 's')
save(fig, '58-262')
