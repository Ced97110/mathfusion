import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
ys = [8 + 13 * i for i in range(5)]
for i in range(4):
    line(ax, [(30, ys[i] + 3.6), (30, ys[i + 1] - 3.6)], 'fixe')
for y, n in zip(ys, [1, 2, 4, 8, 16]):
    disc(ax, 30, y, 3.6, 'sujet', label=str(n), size='s')
line(ax, [(30, ys[-1] + 3.6), (30, 68)], 'fixe', dash=True)
arrow(ax, (30, 68), (30, 82), 'varie')
text(ax, 36, 72, '32, 64, …', 'varie', 's', ha='left')
text(ax, 36, 79, 'aucun dernier nombre', 'varie', 's', ha='left')
save(fig, '79-204')
