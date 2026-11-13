import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
cx = [34, 50, 66]
for x, h in zip(cx, ['unités', 'dixièmes', 'centièmes']): text(ax, x, 88, h, 'fixe', 's')
def row(y, ds, r):
    for x, d in zip(cx, ds): text(ax, x, y, d, r, 'xl', weight='bold')
    text(ax, 42, y - 1.5, ',', r, 'xl', weight='bold')
row(66, '235', 'sujet'); row(52, '180', 'autre')
text(ax, 18, 52, '+', 'encre', 'xl')
line(ax, [(14, 44), (76, 44)], 'encre', lw=1.0)
row(36, '415', 'resultat')
box(ax, 28, 72, 12, 9, 'varie', label='1', size='l')
arrow(ax, (47, 77), (41, 77), 'varie')
text(ax, 62, 77, 'on retient 1', 'varie', 's')
text(ax, 8, 22, 'centièmes : 5 + 0 = 5', 'fixe', 's', ha='left')
text(ax, 8, 14, 'dixièmes : 3 + 8 = 11', 'fixe', 's', ha='left')
text(ax, 8, 6, 'unités : 2 + 1 + 1 = 4', 'fixe', 's', ha='left')
save(fig, '08-061')
