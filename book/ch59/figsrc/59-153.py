import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 2, 84, 68, 'sujet', fill=False, dash=True)
text(ax, 44, 64, 'matrices inversibles (ch. 73)', 'sujet', 's')
labs = ['type I\najouter', 'type II\nmultiplier', 'type III\néchanger']
for i, l in enumerate(labs):
    box(ax, 6 + i * 28, 38, 22, 17, 'varie', label=l, size='s')
    arrow(ax, (17 + i * 28, 37.5), (44 + (i - 1) * 8, 24), 'varie')
box(ax, 18, 10, 52, 13, 'resultat', label='(2, 1) et (1, 1)\ndéterminant 1', size='s')
save(fig, '59-153')
