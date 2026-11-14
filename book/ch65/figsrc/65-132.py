import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'départ', 'sujet', 's')
box(ax, 8, 71, 72, 11, 'sujet', label=r'$\sigma=(1\,2\,3\,4\,5)$ et $(1\,2)$', size='s')
arrow(ax, (44, 71), (44, 60), 'varie')
text(ax, 44, 55, 'étape décisive', 'varie', 's')
box(ax, 8, 38, 72, 12, 'varie', label=r'$\sigma\,(1\,2)\,\sigma^{-1}=(2\,3)$')
arrow(ax, (44, 38), (44, 29), 'resultat')
text(ax, 44, 24, 'arrivée', 'resultat', 's')
xs = [10 + i * 17 for i in range(5)]
for i in range(4):
    line(ax, [(xs[i], 12), (xs[i + 1], 12)], 'resultat', lw=1.6)
    text(ax, (xs[i] + xs[i + 1]) / 2, 6, ['(1 2)', '(2 3)', '(3 4)', '(4 5)'][i], 'resultat', 's')
for i, x in enumerate(xs):
    disc(ax, x, 12, 2.6, 'resultat', label=str(i + 1))
text(ax, 44, 19, r'ces échanges donnent $S_5$', 'resultat', 's')
save(fig, '65-132')
