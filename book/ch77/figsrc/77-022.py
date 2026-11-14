import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(64)
text(ax, 14, 59, '$a$', 'sujet', 'l'); text(ax, 70, 59, r'$a_L$', 'varie', 'l')
for y, a, op in ((44, '$3$', r'multiplier par $3$'), (28, '$i$', r'multiplier par $i$'), (12, '$2+i$', r'multiplier par $2+i$')):
    box(ax, 3, y - 4.5, 22, 9, 'sujet', label=a)
    arrow(ax, (27, y), (54, y), 'varie')
    box(ax, 56, y - 4.5, 30, 9, 'varie', label=op, size='s')
save(fig, '77-022')
