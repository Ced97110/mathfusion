import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [3 + i * 17 for i in range(5)]; w = 13; h = 11
y1, y2 = 44, 16
row1 = {0: '24', 1: '12', 2: '4', 4: '1'}
row2 = ['24', '12', '4', '2', '1']
for i in range(5):
    if i in row1:
        box(ax, xs[i], y1, w, h, 'sujet', label=row1[i], size='l')
    else:
        box(ax, xs[i], y1, w, h, 'varie', fill=False, dash=True)
    box(ax, xs[i], y2, w, h, 'varie' if i == 3 else 'sujet', label=row2[i], size='l')
    cx = xs[i] + w / 2
    if i == 3:
        arrow(ax, (cx, y1 - 0.5), (cx, y2 + h + 0.5), 'varie')
    else:
        line(ax, [(cx, y1 - 0.5), (cx, y2 + h + 0.5)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 63, 'facteurs : 2, 3, 4', 'encre', 's')
text(ax, 44, 3.5, 'facteurs : 2, 3, 2, 2', 'encre', 's')
text(ax, xs[3] + w / 2, 59, 'on intercale 2', 'varie', 's')
save(fig, '64-039')
