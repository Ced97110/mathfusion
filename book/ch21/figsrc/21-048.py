import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 13, 38, r'$\frac{x^2-4}{x-2}$', 'sujet', 'm'); text(ax, 13, 16, r'$x+2$', 'autre', 's')
data = [(0, '2', '2'), (1, '3', '3'), (2, None, '4'), (3, '5', '5')]
for i, (x, a, b) in enumerate(data):
    c = 33.5 + 15 * i
    text(ax, c, 52, rf'$x={x}$', 'encre', 's')
    if a is None:
        disc(ax, c, 38, 4.2, 'limite', fill=False, lw=1.0)
    else:
        disc(ax, c, 38, 4.2, 'sujet', label=a)
    disc(ax, c, 16, 4.2, 'autre', label=b)
    if a is not None: line(ax, [(c, 33.5), (c, 20.5)], 'resultat', lw=1.2)
text(ax, 63.5, 27, 'pas de valeur', 'limite', 's')
text(ax, 44, 5, 'égales partout sauf en 2', 'resultat', 's')
save(fig, '21-048')
