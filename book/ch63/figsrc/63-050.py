import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$\sigma,\tau$ fixent $F$ ; $a\in F$', 'encre', 'm')
xs = [12, 44, 76]
for x in xs:
    disc(ax, x, 53, 4.5, 'resultat', label=r'$a$')
for i, n in enumerate([r'$\tau$', r'$\sigma$']):
    arrow(ax, (xs[i] + 5.5, 53), (xs[i + 1] - 5.5, 53), 'varie')
    text(ax, (xs[i] + xs[i + 1]) / 2, 58, n, 'varie', 'm')
text(ax, 44, 44, r'$\sigma\tau(a)=\sigma(a)=a$', 'resultat', 'm')
for x in xs:
    disc(ax, x, 24, 4.5, 'resultat', label=r'$a$')
arrow(ax, (xs[0] + 5.5, 24), (xs[1] - 5.5, 24), 'varie')
text(ax, 28, 29, r'$\sigma$', 'varie', 'm')
arrow(ax, (xs[1] + 5.5, 24), (xs[2] - 5.5, 24), 'varie', lw=2.0)
text(ax, 60, 29, r'$\sigma^{-1}$', 'varie', 'm', weight='bold')
text(ax, 44, 13, r'$\sigma^{-1}(a)=a$', 'resultat', 'm')
save(fig, '63-050')
