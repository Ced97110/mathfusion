import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'1re case : $10$ divisé par $d=2$', 'encre', 's')
f = numberline(ax, 8, 70, 56, 0, 10, arrow_right=False, size='s', every=2)
for k in range(5):
    arrow(ax, (f(2 * k) + 0.8, 59), (f(2 * k + 2) - 0.8, 59), 'varie', curve=-0.5, lw=0.8)
text(ax, 44, 67, 'quotient 5, reste 0', 'varie', 's')
box(ax, 4, 28, 24, 10, 'sujet', label=r'$(10,\,10)$', size='s')
text(ax, 32, 33, r'$-$', 'varie', 'l')
box(ax, 36, 28, 28, 10, 'varie', label=r'$5\times(2,\,8)$', size='s')
text(ax, 68, 33, r'$=$', 'encre', 'l')
box(ax, 72, 28, 14, 10, 'resultat', label=r'$(0,\,-30)$', size='s')
text(ax, 44, 12, '1re case nulle : il reste 1 case', 'resultat', 's')
save(fig, '59-026')
