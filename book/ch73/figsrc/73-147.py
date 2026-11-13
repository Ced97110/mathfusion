import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(82)
text(ax, 44, 77.5, 'étage du haut : on garde la matrice', 'sujet', 's')
box(ax, 3, 60, 82, 13, 'sujet')
text(ax, 14, 66.5, r'$O(n)$', 'sujet', 'l'); text(ax, 56, 66.5, r'$A$ = quart de tour', 'sujet', 'm')
box(ax, 3, 14, 82, 26, 'fixe')
text(ax, 14, 35, r'$E(n)$', 'fixe', 'l'); text(ax, 56, 35, r'couples $(A,\ x)$', 'fixe', 'm')
box(ax, 8, 18, 33, 10, 'varie', label=r'$(A,\ (3,\ 1))$')
box(ax, 47, 18, 33, 10, 'varie', label=r'$(A,\ (5,\ 0))$')
arrow(ax, (24, 40), (34, 60), 'varie', lw=1.6); arrow(ax, (64, 40), (54, 60), 'varie', lw=1.6)
text(ax, 44, 50, r'$(A,x)\mapsto A$', 'varie', 'l')
text(ax, 44, 8, 'même A, décalages différents', 'encre', 's')
save(fig, '73-147')
