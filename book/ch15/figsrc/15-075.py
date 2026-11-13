import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
A = [(r'$-50x$', 'autre'), (r'$9x^{2}$', 'sujet'), (r'$-13$', 'fixe')]
B = [A[1], A[0], A[2]]
for i, (l, r) in enumerate(A): box(ax, 4 + i * 22, 50, 20, 10, r, label=l, size='s')
for i, (l, r) in enumerate(B): box(ax, 4 + i * 22, 14, 20, 10, r, label=l, size='s')
arrow(ax, (14, 49), (36, 25), 'varie'); arrow(ax, (36, 49), (14, 25), 'varie')
arrow(ax, (58, 49), (58, 25), 'fixe')
text(ax, 78, 55, r'$=-77$', 'resultat', 'm'); text(ax, 78, 19, r'$=-77$', 'resultat', 'm')
text(ax, 44, 67, r'pour $x=2$', 'encre', 's')
text(ax, 44, 5, 'même polynôme, autre ordre', 'resultat', 's')
save(fig, '15-075')
