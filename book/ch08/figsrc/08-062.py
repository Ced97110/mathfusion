import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx = [36, 52, 68]
for x, h in zip(cx, ['unités', 'dixièmes', 'centièmes']): text(ax, x, 76, h, 'fixe', 's')
def row(y, ds, roles, lab, lr):
    text(ax, 12, y, lab, lr, 'l', weight='bold')
    for x, d, r in zip(cx, ds, roles):
        if d is None: box(ax, x - 6, y - 5, 12, 10, 'fixe', fill=False, dash=True)
        else: box(ax, x - 6, y - 5, 12, 10, r, label=d, size='l')
    text(ax, (cx[0] + cx[1]) / 2, y - 3, ',', lr, 'l', weight='bold')
row(60, '235', ['sujet'] * 3, '2,35', 'sujet')
row(42, ['1', '8', None], ['autre'] * 3, '1,8', 'autre')
row(20, '180', ['autre', 'autre', 'varie'], '1,80', 'autre')
arrow(ax, (68, 36), (68, 26), 'varie')
text(ax, 50, 31, 'même nombre', 'varie', 's')
save(fig, '08-062')
