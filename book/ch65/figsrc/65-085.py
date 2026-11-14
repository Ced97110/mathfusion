import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 50, 32, 10, 'sujet', label='racines 1, 2, 3, 4', size='s')
box(ax, 2, 12, 32, 10, 'sujet', label='racines 2, 1, 3, 4', size='s')
arrow(ax, (8, 49), (8, 23), 'varie')
text(ax, 22, 36, r'échange $r_1$, $r_2$', 'varie', 's')
top = [r'$t_1=14$', r'$t_2=11$', r'$t_3=10$']
bot = [r'$t_1=14$', r'$t_2=10$', r'$t_3=11$']
xs = [40, 56, 72]
for i in range(3):
    box(ax, xs[i], 50, 14, 10, 'fixe', label=top[i], size='s')
    box(ax, xs[i], 12, 14, 10, 'fixe' if i == 0 else 'varie', label=bot[i], size='s')
arrow(ax, (47, 49), (47, 23), 'fixe')
arrow(ax, (63, 49), (79, 23), 'varie')
arrow(ax, (79, 49), (63, 23), 'varie')
text(ax, 62, 36, '', 'fixe', 's')
text(ax, 44, 4, r'$t_2$ et $t_3$ se sont échangés', 'varie', 's')
save(fig, '65-085')
