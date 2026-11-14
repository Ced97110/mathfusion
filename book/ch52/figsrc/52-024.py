import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$4k+r$ avec $r=3$', 'sujet', 'l')
for x, k in zip([14, 34, 54, 74], [-1, 0, 1, 2]):
    text(ax, x, 48, r'$k=%d$' % k, 'varie', 'm')
    arrow(ax, (x, 44), (x, 38), 'fixe')
    text(ax, x, 33, r'$%d\times4+3$' % k if k >= 0 else r'$(-1)\times4+3$', 'encre', 's')
    arrow(ax, (x, 29), (x, 23), 'fixe')
    disc(ax, x, 17, 4.3, 'limite', label=str(4 * k + 3).replace('-', '−'), size='m')
text(ax, 44, 4, 'tous les entiers de la classe', 'limite', 's')
save(fig, '52-024')
