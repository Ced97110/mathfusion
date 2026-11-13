import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [6, 20, 34]
for i, x in enumerate(xs):
    box(ax, x, 24, 10, 10, 'sujet', label=str(i + 1), size='l')
box(ax, 48, 24, 12, 10, 'varie', label='…', size='l')
for i in range(3):
    a = xs[i] + 5; b = (xs + [48])[i + 1] + (5 if i < 2 else 6)
    arrow(ax, (a, 34.5), (b, 34.5), 'varie', curve=-0.6)
    text(ax, (a + b) / 2, 41, '+1', 'varie', 's')
arrow(ax, (61, 29), (84, 29), 'varie')
brace(ax, 48, 84, 22, 'varie', label='et ainsi de suite, sans fin')
save(fig, '12-069')
