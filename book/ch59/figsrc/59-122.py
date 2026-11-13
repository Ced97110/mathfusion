import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
bx = [4 + 8.2 * i + 3.8 for i in range(10)]   # centres des 10 restes v
tx = [33, 55]                                  # centres des 2 restes u
yt, yb = 56, 22
for i, xt in enumerate(tx):
    for j, xb in enumerate(bx):
        hl = (i == 1 and j == 7)
        if not hl:
            line(ax, [(xt, yt - 3.5), (xb, yb + 3)], 'fixe', lw=0.4)
line(ax, [(tx[1], yt - 3.5), (bx[7], yb + 3)], 'varie', lw=1.6)
for i, xt in enumerate(tx):
    box(ax, xt - 7, yt - 3.5, 14, 7, 'sujet', label=f'u = {i}', size='s')
for j, xb in enumerate(bx):
    box(ax, xb - 3.8, yb - 3, 7.6, 6, 'autre', label=('v = 0' if j == 0 else str(j)), size='s', r=0.6)
t = text(ax, 71, 40, '(1, 7)', 'varie', 's', weight='bold')
t.set_bbox(dict(fc='white', ec='none', pad=1.2))
text(ax, 44, 70, '2 × 10 = 20 couples', 'encre', 'm', weight='bold')
save(fig, '59-122')
