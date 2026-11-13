import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 6, 52, 'idéal nul : le plus petit', 'autre', 's', ha='left')
text(ax, 6, 27, 'idéal total : le plus grand', 'sujet', 's', ha='left')
for i in range(6):
    x = 6 + i * 13
    if i == 0: box(ax, x, 37, 11, 9, 'autre', label='0')
    else: box(ax, x, 37, 11, 9, 'fixe', dash=True, fill=False)
    box(ax, x, 14, 11, 9, 'varie' if i == 1 else 'sujet', label=str(i))
arrow(ax, (24.5, 7), (24.5, 13), 'varie')
text(ax, 24.5, 4, 'contient 1', 'varie', 's')
save(fig, '52-271')
