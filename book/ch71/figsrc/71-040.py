import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 6, 48, 30, 10, 'sujet', label=r'$3\,e_1$'); text(ax, 44, 53, '+', 'encre', 'l'); box(ax, 52, 48, 30, 10, 'autre', label=r'$5\,e_2$')
text(ax, 44, 41, r'on applique $e_1^*$', 'varie', 's')
arrow(ax, (21, 47), (21, 36), 'varie'); arrow(ax, (67, 47), (67, 36), 'varie')
box(ax, 6, 26, 30, 10, 'sujet', label=r'$3\times 1$'); text(ax, 44, 31, '+', 'encre', 'l'); box(ax, 52, 26, 30, 10, 'fixe', label=r'$5\times 0$')
arrow(ax, (21, 25), (36, 13), 'fixe'); arrow(ax, (67, 25), (52, 13), 'fixe')
box(ax, 30, 3, 28, 10, 'resultat', label='3', size='l')
save(fig, '71-040')
