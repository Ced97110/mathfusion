import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def d(x, y, s, r): disc(ax, x, y, 3.2, r, label=s, size='m')
text(ax, 44, 83, 'deux éléments, une classe', 'varie', 'm', weight='bold')
d(12, 72, '3', 'fixe'); d(12, 58, '15', 'fixe'); box(ax, 56, 59, 18, 11, 'sujet', label=r'$\bar{3}$', size='l')
arrow(ax, (15.5, 71), (55.5, 66), 'varie'); arrow(ax, (15.5, 59), (55.5, 63), 'varie')
text(ax, 80, 64.5, r'$\nu$', 'varie', 'l')
text(ax, 44, 46, 'classes seules : une flèche chacune', 'resultat', 's', weight='bold')
for i, (n, y) in enumerate(zip(['1', '2', '3'], [37, 25, 13])):
    d(12, y, n, 'fixe'); box(ax, 56, y - 5, 18, 10, 'sujet', label=r'$\bar{%s}$' % n, size='l')
    arrow(ax, (15.5, y), (55.5, y), 'resultat')
text(ax, 80, 25, 'injective', 'resultat', 's')
text(ax, 44, 2.5, 'chaque classe reçoit une flèche', 'sujet', 's')
save(fig, '43-083')
