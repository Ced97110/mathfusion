import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [4, 34, 64]
box(ax, xs[0], 24, 20, 10, 'sujet', label='(2, 1)', size='m')
box(ax, xs[1], 24, 20, 10, 'varie', label='(2, −1)', size='m')
box(ax, xs[2], 24, 20, 10, 'resultat', label='(−1, 2)', size='m')
arrow(ax, (xs[0] + 20.5, 29), (xs[1] - 0.5, 29), 'varie')
arrow(ax, (xs[1] + 20.5, 29), (xs[2] - 0.5, 29), 'varie')
text(ax, 29, 33, 'pli 1', 'varie', 's'); text(ax, 59, 33, 'pli 2', 'varie', 's')
text(ax, 29, 19, r'$u_1 = (0, 1)$', 'encre', 's'); text(ax, 59, 19, r'$u_2 = (1, -1)$', 'encre', 's')
text(ax, 29, 12, r'retire $2 \times u_1$', 'varie', 's'); text(ax, 59, 12, r'retire $3 \times u_2$', 'varie', 's')
arrow(ax, (14, 37), (74, 37), 'resultat', curve=-0.18)
text(ax, 44, 48, r'$S_{u_2}\,S_{u_1}$', 'resultat', 'l')
save(fig, '72-135')
