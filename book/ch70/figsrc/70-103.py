import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'première ligne du tableau', 'varie', 's')
xs = [1.5, 30.5, 59.5]
for x, t in zip(xs, ['1', '0', r'$x^2-4$']):
    box(ax, x, 54, 27, 11, 'varie', label=t)
    arrow(ax, (x + 13.5, 53.5), (x + 13.5, 44.5), 'varie', lw=1.0)
text(ax, 44, 42, 'fois le déterminant 2 × 2 restant', 'fixe', 's')
for x, t, r in zip(xs, [r'$1\times(2-x^2)^2$', r'$0\times\ldots=0$', r'$(x^2-4)\times1$'], ['sujet', 'fixe', 'sujet']):
    box(ax, x, 26, 27, 11, r, label=t, size='s')
    arrow(ax, (x + 13.5, 25.5), (44, 17.5), 'fixe', lw=0.7)
box(ax, 12, 4, 64, 12, 'resultat', label=r'$(2-x^2)^2+x^2-4$')
save(fig, '70-103')
