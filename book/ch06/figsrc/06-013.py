import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 12, 36, '3', 'varie', 'l')
line(ax, [(6, 31.5), (18, 31.5)], 'encre', lw=1.2)
text(ax, 12, 27, '4', 'fixe', 'l')
for j in range(4):
    box(ax, 26 + j * 14, 36, 14, 8, 'varie' if j < 3 else 'fixe', r=0.3)
    box(ax, 26 + j * 14, 14, 14, 8, 'fixe', r=0.3)
arrow(ax, (18, 27), (25, 21), 'fixe')
arrow(ax, (18, 36), (25, 39), 'varie')
arrow(ax, (54, 24), (54, 34), 'varie')
text(ax, 54, 50, '2. ensuite : on en prend 3', 'varie')
text(ax, 54, 8, "1. d'abord : coupé en 4", 'fixe')
save(fig, '06-013')
