import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$(r_2\ r_3)$ avec 5 racines', 'varie', 'l')
xs = [10 + 17 * i for i in range(5)]
for i, x in enumerate(xs):
    role = 'sujet' if i in (1, 2) else 'fixe'
    disc(ax, x, 38, 4.2, role, label=f'$r_{i + 1}$', size='m')
    disc(ax, x, 12, 4.2, role)
for i in (0, 3, 4):
    arrow(ax, (xs[i], 33.5), (xs[i], 16.7), 'fixe')
arrow(ax, (xs[1] + 1.5, 33.7), (xs[2] - 1.5, 16.3), 'varie')
arrow(ax, (xs[2] - 1.5, 33.7), (xs[1] + 1.5, 16.3), 'varie')
text(ax, 18, 25, '3 restent', 'fixe', 's')
text(ax, 62, 25, '2 échangées', 'varie', 's')
save(fig, '65-031')
