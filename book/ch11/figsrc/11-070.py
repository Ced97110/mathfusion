import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
xs = (28, 52)
text(ax, xs[0], 72, 'h', 'fixe', 'm'); text(ax, xs[1], 72, 'min', 'fixe', 'm')
rows = [(60, '2', '40', 'sujet'), (49, '1', '35', 'autre'), (38, '3', '75', 'varie')]
for y, a, b, r in rows:
    box(ax, xs[0] - 8, y, 16, 9, r, label=a, size='m'); box(ax, xs[1] - 8, y, 16, 9, r, label=b, size='m')
text(ax, 12, 53.5, '+', 'encre', 'l')
arrow(ax, (xs[1], 37), (xs[1], 31), 'varie')
text(ax, 76, 34, '75 = 1 h 15', 'varie', 's', ha='right')
box(ax, xs[0] - 8, 17, 16, 9, 'resultat', label='4', size='m'); box(ax, xs[1] - 8, 17, 16, 9, 'resultat', label='15', size='m')
arrow(ax, (xs[1] - 9, 36), (xs[0] + 1, 27), 'varie', curve=0.0)
save(fig, '11-070')
