import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
disc(ax, 11, 34, 4, 'limite', label='3', size='m')
text(ax, 11, 24, 'le nombre 3', 'limite', 's')
arrow(ax, (18, 34), (30, 34), 'varie')
text(ax, 24, 40, 'la barre', 'varie', 's')
box(ax, 33, 14, 53, 40, 'limite', fill=False, dash=True)
for x, s in zip([40, 51, 62, 73], ['−1', '3', '7', '11']):
    disc(ax, x, 40, 4, 'limite', label=s, size='s')
text(ax, 82.5, 40, '…', 'limite', 'm')
text(ax, 59.5, 24, r'$\bar{3}$ : tout le paquet', 'limite', 'l')
save(fig, '52-023')
