import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
xs = [4 + i * 16 for i in range(4)]
for x, v in zip(xs, '0123'): box(ax, x, 10, 12, 12, 'sujet', label=v, size='m')
for i in range(3): arrow(ax, (xs[i] + 6, 24), (xs[i + 1] + 6, 24), 'varie', curve=-0.6)
text(ax, 75, 16, '…', 'sujet', 'l')
arrow(ax, (63, 17), (72, 17), 'fixe', lw=0.8)
for i in range(3): text(ax, xs[i] + 14, 35, '+1', 'varie', 's')
text(ax, 44, 3.5, 'toujours un suivant', 'sujet', 's')
save(fig, '44-091')
