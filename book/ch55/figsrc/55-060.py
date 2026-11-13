import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xs = [18, 44, 70]; yt, yb = 74, 46
text(ax, 44, 82, r'$\pi$ : 1 → 2, 2 → 3, 3 → 1', 'varie', 'm')
pi = {0: 1, 1: 2, 2: 0}
for i, x in enumerate(xs):
    disc(ax, x, yt, 4.6, 'sujet', label=rf'$x_{i+1}$')
    disc(ax, xs[i], yb, 4.6, 'autre', label=rf'$x_{i+1}$')
for i in range(3):
    arrow(ax, (xs[i], yt - 4.8), (xs[pi[i]], yb + 4.8), 'varie')
text(ax, 6, yt, 'avant', 'sujet', 's')
text(ax, 6, yb, 'après', 'autre', 's')
box(ax, 6, 14, 32, 12, 'sujet', label=r'$x_1^2\,x_2$')
box(ax, 50, 14, 32, 12, 'autre', label=r'$x_2^2\,x_3$')
arrow(ax, (38, 20), (50, 20), 'varie')
text(ax, 44, 29, 'renommer', 'varie', 's')
text(ax, 44, 6, 'seuls les noms changent', 'fixe', 's')
save(fig, '55-060')
