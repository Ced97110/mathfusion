import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(44, 'fixe', 'cos x', 'sécante', '1 ÷'), (24, 'sujet', 'sin 30° = 0,5', 'cosécante', '1 ÷ 0,5 = 2'), (4, 'fixe', 'tan x', 'cotangente', '1 ÷')]
for y, r, a, b, c in rows:
    box(ax, 3, y, 24, 14, r, label=a); box(ax, 56, y, 29, 14, r, label=b)
    arrow(ax, (28, y + 7), (55, y + 7), 'varie')
    text(ax, 41.5, y + 11, c, 'varie', 's')
save(fig, '30-073')
