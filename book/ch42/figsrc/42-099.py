import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 14, 52, 60, 14, 'varie', label='on suppose l’énoncé faux', size='m')
box(ax, 14, 28, 60, 14, 'limite', label=r'on obtient : $n > n$', size='m')
box(ax, 14, 4, 60, 14, 'resultat', label='donc l’énoncé est vrai', size='m')
arrow(ax, (44, 52), (44, 43), 'fixe'); arrow(ax, (44, 28), (44, 19), 'fixe')
text(ax, 47, 47.5, 'on déduit', 'fixe', 's', ha='left'); text(ax, 47, 23.5, 'c’est impossible', 'limite', 's', ha='left')
save(fig, '42-099')
