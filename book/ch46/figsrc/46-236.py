import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$|A_3| = 6/2 = 3$', 'resultat', 'l')
box(ax, 2, 10, 84, 28, 'sujet', fill=False)
text(ax, 5, 34.5, r'$A_3$', 'sujet', 'm', ha='left')
for i, l in enumerate(['id', '(1 2 3)', '(1 3 2)']): box(ax, 6 + i * 27, 15, 22, 10, 'sujet', label=l, size='s')
for i in range(2): arrow(ax, (28.5 + i * 27, 20), (32.5 + i * 27, 20), 'varie')
text(ax, 44, 5, r'chaque pas : $\times (1\ 2\ 3)$', 'varie', 's')
save(fig, '46-236')
