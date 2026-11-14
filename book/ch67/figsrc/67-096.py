import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [24, 64]
for x, v in zip(xs, ('0', '1')):
    disc(ax, x, 50, 6, 'resultat', label=v, size='l')
    arrow(ax, (x, 43), (x, 24), 'resultat', lw=1.2)
    disc(ax, x, 17, 6, 'resultat', label=v, size='l')
    text(ax, x, 5, v + r'$^2$ = ' + v, 'resultat', 'l')
text(ax, 4, 50, '$x$', 'encre', 's', ha='left'); text(ax, 4, 17, '$x^2$', 'encre', 's', ha='left')
text(ax, 44, 33, 'même place', 'resultat', 's')
save(fig, '67-096')
