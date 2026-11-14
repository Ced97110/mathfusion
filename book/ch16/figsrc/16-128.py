import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 84, 'calcul valable pour tout $y$', 'sujet', 's')
box(ax, 6, 66, 76, 11, 'sujet', label=r'$-2(10 - 2y) - 4y + 1 = -18$', size='m')
arrow(ax, (44, 66), (44, 59), 'varie'); text(ax, 48, 62.5, 'distribue −2', 'varie', 's', ha='left')
box(ax, 6, 47, 76, 11, 'sujet', label=r'$-20 + 4y - 4y + 1 = -18$', size='m')
arrow(ax, (44, 47), (44, 40), 'varie'); text(ax, 48, 43.5, r'$4y - 4y = 0$', 'varie', 's', ha='left')
box(ax, 22, 29, 44, 10, 'limite', label=r'$-19 = -18$ : faux', size='m')
text(ax, 44, 22, 'à gauche : toujours −19', 'fixe', 's')
for i, v in enumerate(['0', '1', '5']):
    box(ax, 4 + i * 28, 4, 26, 14, 'fixe', label=rf'$y = {v}$' + '\n−19', size='s')
save(fig, '16-128')
