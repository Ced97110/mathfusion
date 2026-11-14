import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 20, 50, 48, 10, 'sujet', label='Groupe de 12 éléments', size='s')
for k, v in enumerate(['1', '2', '3', '4', '6', '12']):
    box(ax, 4 + k*14, 10, 12, 10, 'fixe', label=v, size='m')
arrow(ax, (26, 49), (26, 21.5), 'sujet')
text(ax, 28, 38, 'Lagrange :', 'sujet', 's', ha='left'); text(ax, 28, 33, 'tailles possibles', 'sujet', 's', ha='left')
arrow(ax, (82, 21.5), (82, 49), 'varie')
text(ax, 80, 40, 'Sylow :', 'varie', 's', ha='right'); text(ax, 80, 35, 'lesquelles', 'varie', 's', ha='right'); text(ax, 80, 30, 'existent ?', 'varie', 's', ha='right')
save(fig, '47-205')
