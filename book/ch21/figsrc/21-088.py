import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 82, 'chaque bas mis égal à 0', 'sujet', 's')
for cx, d, e, v, val in ((21, r'$x-1$', r'$x-1=0$', r'$x=1$', 1), (67, r'$x+6$', r'$x+6=0$', r'$x=-6$', -6)):
    box(ax, cx - 12, 62, 24, 10, 'sujet', True, d)
    arrow(ax, (cx, 61.5), (cx, 52), 'varie')
    box(ax, cx - 12, 42, 24, 10, 'fixe', True, e)
    arrow(ax, (cx, 41.5), (cx, 32), 'varie')
    box(ax, cx - 12, 22, 24, 10, 'varie', True, v)
f = numberline(ax, 6, 80, 8, -7, 3, 1, labels=False, arrow_right=False)
for v, t in ((-6, r'$-6$'), (0, r'$0$'), (1, r'$1$')):
    text(ax, f(v), 3, t, 'fixe', 's')
for v in (-6, 1):
    disc(ax, f(v), 8, 1.5, 'varie')
save(fig, '21-088')
