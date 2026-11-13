import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 31, 52, 'produit de cisaillements', 'sujet', 's')
for x in (3, 24, 45): box(ax, x, 36, 15, 10, 'sujet', label='dét. 1', size='s')
text(ax, 21, 41, r'$\times$', 'encre', 'l'); text(ax, 42, 41, r'$\times$', 'encre', 'l'); text(ax, 63, 41, '=', 'encre', 'l')
box(ax, 67, 36, 18, 10, 'resultat', label='dét. 1', size='m')
box(ax, 22, 6, 44, 10, 'limite', label='dilatation : dét. 2', size='m')
arrow(ax, (76, 35), (63, 17), 'limite'); text(ax, 52, 26, r'$1\neq 2$', 'limite', 'l')
save(fig, '73-155')
