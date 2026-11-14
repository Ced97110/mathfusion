import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 3, 22, 28, 18, 'autre', label='négatifs', size='m')
box(ax, 34, 22, 20, 18, 'fixe', label='0', size='xl')
box(ax, 57, 22, 28, 18, 'sujet', label='positifs', size='m')
text(ax, 17, 15, 'à gauche de 0', 'autre', 's'); text(ax, 71, 15, 'à droite de 0', 'sujet', 's')
text(ax, 44, 15, 'pas à gauche', 'limite', 's'); text(ax, 44, 9, 'pas à droite', 'limite', 's')
save(fig, '12-064')
