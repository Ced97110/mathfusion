import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 34, 44, 20, 11, 'sujet', label=r'$x$', size='xl')
text(ax, 71, 49.5, 'même lettre', 'sujet', 's')
for i, (v, n) in enumerate([('35', 'rue 1'), ('25', 'rue 2'), ('10', 'rue 3')]):
    cx = 16 + 28 * i
    disc(ax, cx, 22, 8, 'varie', label=r'$x=%s$' % v, size='m')
    text(ax, cx, 10, n, 'fixe', 's')
    arrow(ax, (44, 44), (cx, 30.5), 'sujet')
save(fig, '12-001')
