import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ys = [16, 40, 64]
L = ["sous-groupe d'ordre 1", "sous-groupe d'ordre 2", "sous-groupe d'ordre 4"]
R = ['petit corps', 'corps du milieu', 'grand corps']
text(ax, 20, 78, "groupe cyclique d'ordre 4", 'sujet', 's'); text(ax, 68, 78, 'corps', 'autre', 's')
for y, a in zip(ys, L): box(ax, 2, y - 5, 36, 10, 'sujet', label=a, size='s')
for y, b in zip(ys, R): box(ax, 52, y - 5, 34, 10, 'autre', label=b, size='s')
# order 1 (bottom) <-> grand corps (top), order 4 (top) <-> petit corps (bottom)
for i in range(3): arrow(ax, (39, ys[i]), (51, ys[2 - i]), 'varie', both=True)
for a, b in ((0, 1), (1, 2)):
    arrow(ax, (20, ys[a] + 5.5), (20, ys[b] - 5.5), 'fixe'); arrow(ax, (69, ys[a] + 5.5), (69, ys[b] - 5.5), 'fixe')
text(ax, 44, 4, 'le plus grand sous-groupe donne le plus petit corps', 'varie', 's')
save(fig, '67-103')
