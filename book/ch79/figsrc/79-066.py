import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
ys = {k: 10 + 17 * k for k in range(5)}
arrow(ax, (8, 4), (8, 84), 'fixe')
for k, y in ys.items():
    line(ax, [(6.5, y), (9.5, y)], 'fixe')
    text(ax, 3, y, str(k), 'fixe', 's')
    line(ax, [(10, y), (84, y)], 'fixe', lw=0.4, dash=True)
text(ax, 8, 87, 'étage', 'fixe', 's')
nodes = [(1, 0, 24), (5, 1, 34), (4, 2, 44), (60, 4, 54)]
for n, k, x in nodes:
    disc(ax, x, ys[k], 4.2, 'sujet', label=str(n))
    text(ax, x + 6, ys[k] + 4.5, f'$d({n}) = {k}$', 'varie', 's', ha='left')
save(fig, '79-066')
