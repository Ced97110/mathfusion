import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 24, 46, 40, 12, 'autre', label='lemme', size='m', weight='bold')
text(ax, 44, 41.5, 'prouvé une seule fois', 'autre', 's')
box(ax, 2, 4, 84, 30, 'fixe', fill=False, dash=True)
for x in (6, 34, 62):
    box(ax, x, 12, 20, 12, 'autre', label='lemme cité', size='s')
    arrow(ax, (44, 37), (x + 10, 25.5), 'varie')
text(ax, 44, 7.5, 'preuve longue d’un théorème', 'fixe', 's')
save(fig, '42-103')
