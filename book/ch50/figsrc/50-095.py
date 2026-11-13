import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 3, 84, 54, 'fixe', fill=False, dash=True)
text(ax, 8, 51, r'$\Pi$', 'encre', 'l', weight='bold')
text(ax, 55, 51, '2 éléments → 2 éléments', 'resultat', 's')
xs = [8, 36, 64]
for k, x in zip('ABC', xs):
    box(ax, x, 24, 18, 14, 'sujet')
    for dx in (5, 13): disc(ax, x + dx, 31, 2.4, 'sujet')
    text(ax, x + 9, 41.5, r'$P_%s$' % k, 'sujet', 's')
arrow(ax, (xs[0] + 9, 22.5), (xs[1] + 9, 22.5), 'varie', lw=1.2, curve=0.45)
text(ax, 31, 9, r'$g = r$ : $gPg^{-1}$', 'varie', 's')
save(fig, '50-095')
