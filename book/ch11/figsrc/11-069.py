import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y = 42
for i, (d, n) in enumerate(zip('345', ['centaines', 'dizaines', 'unités'])):
    x = 10 + i * 26
    box(ax, x, y, 16, 12, 'sujet', label=d, size='l'); text(ax, x + 8, y - 3.5, n, 'sujet', 's')
    if i: arrow(ax, (x - 1, y + 6), (x - 8, y + 6), 'varie'); text(ax, x - 4.5, y + 10, '×10', 'varie', 's')
y = 8
for i, (v, n) in enumerate([('2 h', 'heures'), ('40 min', 'minutes')]):
    x = 14 + i * 36; w = 22 if i else 16
    box(ax, x, y, w, 12, 'autre', label=v, size='m'); text(ax, x + w / 2, y - 3.5, n, 'autre', 's')
arrow(ax, (49, y + 6), (31, y + 6), 'varie'); text(ax, 40, y + 10, '×60', 'varie', 's')
save(fig, '11-069')
