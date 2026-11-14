import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
x, y = 1, 2
s = (x + y) % 3
d = int(x != y)
w = int(s != 0)
assert (x + y, s, d, w) == (3, 0, 1, 0) and d != w
box(ax, 4, 74, 80, 14, 'sujet', label=r'$d(x, y) = w(x + y)$', size='l', weight='bold')
text(ax, 44, 69, r'$w$ : nombre de positions non nulles', 'fixe', 's')
text(ax, 44, 64, 'vrai pour des bits, où $1 + 1 = 0$', 'resultat', 's')
line(ax, [(2, 59), (86, 59)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 55, 'essai modulo 3 : 0, 1, 2', 'encre', 'm', weight='bold')
box(ax, 14, 38, 14, 9, 'sujet', label=r'$x = 1$', size='m')
box(ax, 60, 38, 14, 9, 'autre', label=r'$y = 2$', size='m')
text(ax, 44, 42.5, r'$x \neq y$', 'encre', 'm')
arrow(ax, (21, 36.5), (21, 28.5), 'varie')
arrow(ax, (67, 36.5), (67, 32.5), 'varie')
box(ax, 4, 18, 38, 10, 'varie', label=r'$d(x, y) = 1$', size='m')
box(ax, 48, 24, 38, 8.5, 'varie', label=r'$x + y = 3$, reste 0', size='s')
arrow(ax, (67, 23.5), (67, 19.5), 'varie')
box(ax, 48, 10.5, 38, 8.5, 'varie', label=r'$w(x + y) = 0$', size='m')
text(ax, 44, 4, r'$1 \neq 0$ : l’égalité est fausse', 'limite', 'm', weight='bold')
save(fig, '68-050')
