import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
bw = 16
xs = [10, 38, 66]
for x, v, role in zip(xs, ['100', '10', '1'], ['fixe', 'fixe', 'sujet']):
    box(ax, x, 18, bw, 14, role, label=v, size='l')
for i in (0, 1):
    a, b = xs[i + 1] + bw / 2, xs[i] + bw / 2
    arrow(ax, (a, 38), (b, 38), 'varie')
    text(ax, (a + b) / 2, 42, r'$\times 10$', 'varie', 'm')
    arrow(ax, (b, 12), (a, 12), 'autre')
    text(ax, (a + b) / 2, 7, r'$\div 10$', 'autre', 'm')
save(fig, '08-010')
