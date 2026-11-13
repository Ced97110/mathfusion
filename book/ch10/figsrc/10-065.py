import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = lambda v: 8 + v * 72
line(ax, [(8, 20), (80, 20)], 'fixe')
for v, l in [(0, '0'), (.25, '1/4'), (.5, '1/2'), (.75, '3/4'), (1, '1')]:
    disc(ax, f(v), 20, 1.6, 'fixe')
    text(ax, f(v), 14.5, l, 'fixe', 'm')
brace(ax, f(0), f(1), 11, 'fixe', label='5 repères fixes', down=True)
text(ax, 3, 36, 'estimées', 'varie', 's', ha='left')
for v, l, t in [(.6, '3/5', .5), (.9, '9/10', 1)]:
    disc(ax, f(v), 36, 1.6, 'varie')
    text(ax, f(v), 41, l, 'varie', 'm')
    arrow(ax, (f(v), 34), (f(t), 22), 'varie')
save(fig, '10-065')
