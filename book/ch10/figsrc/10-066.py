import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(38)
f = lambda v: 8 + v * 72
line(ax, [(8, 16), (80, 16)], 'fixe')
for v, l in [(0, '0'), (.5, '1/2'), (1, '1')]:
    disc(ax, f(v), 16, 1.6, 'fixe')
    text(ax, f(v), 10.5, l, 'fixe', 'm')
a, b = f(5 / 12), f(.6)
for x, l in [(a, '5/12'), (b, '3/5')]:
    disc(ax, x, 16, 1.4, 'varie')
    text(ax, x, 21, l, 'varie', 'm')
line(ax, [(f(.5), 18), (f(.5), 28)], 'fixe', dash=True)
arrow(ax, (a, 28), (f(.5) - .3, 28), 'varie')
arrow(ax, (b, 28), (f(.5) + .3, 28), 'varie')
text(ax, a - 1.5, 28, '+1/12', 'varie', 's', ha='right')
text(ax, b + 1.5, 28, '−1/10', 'varie', 's', ha='left')
text(ax, 44, 34, '5/12 monte, 3/5 descend', 'encre', 's')
save(fig, '10-066')
