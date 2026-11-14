import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
vals = [14, 24, 34, 44]
for i, v in enumerate(vals):
    x = 5 + 20 * i
    role = 'varie' if i == 2 else 'sujet'
    box(ax, x, 16, 16, 12, role, label=str(v), size='l')
    text(ax, x + 8, 34, r'$x_{(%d)}$' % (i + 1), role, 'l')
    text(ax, x + 8, 10, 'place %d' % (i + 1), role, 's')
    arrow(ax, (x + 8, 32), (x + 8, 28.6), role, lw=0.7)
save(fig, '10-082')
