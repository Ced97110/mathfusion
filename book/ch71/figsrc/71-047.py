import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 24, 50, 40, 10, 'fixe', label='point (3 ; 1)')
arrow(ax, (36, 49), (21, 39), 'varie'); arrow(ax, (52, 49), (67, 39), 'varie')
box(ax, 4, 28, 34, 10, 'sujet', label=r'$s = 2$'); box(ax, 50, 28, 34, 10, 'autre', label=r'$t = 1$')
text(ax, 21, 23, r'coordonnée sur $u_1$', 'sujet', 's'); text(ax, 67, 23, r'coordonnée sur $u_2$', 'autre', 's')
arrow(ax, (21, 17), (36, 13), 'fixe'); arrow(ax, (67, 17), (52, 13), 'fixe')
box(ax, 12, 3, 64, 10, 'resultat', label=r'$2u_1 + 1u_2 = (3\,;\,1)$', size='s')
save(fig, '71-047')
