import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# convention 1 : comparaison
text(ax, 44, 74, r'comparer : $-\infty < 3$', 'varie', 'm')
y = 56
f = numberline(ax, 34, 70, y, 0, 3, arrow_right=True)
disc(ax, 12, y, 4.5, 'sujet', label=r'$-\infty$', size='s')
line(ax, [(17.5, y), (32, y)], 'sujet', dash=True)
disc(ax, f(3), y, 1.8, 'fixe')
text(ax, 44, 40, r'$-\infty$ est à gauche de $3$', 'sujet', 's')
line(ax, [(4, 33), (84, 33)], 'fixe', dash=True)
# convention 2 : addition
text(ax, 44, 27, r'additionner : $-\infty + 3 = -\infty$', 'varie', 'm')
box(ax, 6, 8, 20, 10, 'sujet', label=r'$-\infty$')
text(ax, 31, 13, '+', 'encre', 'l')
box(ax, 36, 8, 14, 10, 'fixe', label='3')
text(ax, 55, 13, '=', 'encre', 'l')
box(ax, 60, 8, 20, 10, 'sujet', label=r'$-\infty$')
save(fig, '54-128')
