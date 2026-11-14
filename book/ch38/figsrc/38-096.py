import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
u = 11.0                     # 1 unité = 11 mm
o = (12.0, 14.0)
f = lambda x, y: (o[0] + u * x, o[1] + u * y)
# quadrillage : 4 sur 3 cases
for i in range(5):
    line(ax, [f(i, 0), f(i, 3)], 'fixe', lw=0.4)
for j in range(4):
    line(ax, [f(0, j), f(4, j)], 'fixe', lw=0.4)
poly(ax, [f(0, 0), f(4, 0), f(4, 3), f(0, 3)], 'autre', fill=False, lw=1.0)
poly(ax, [f(0, 0), f(4, 0), f(0, 3)], 'sujet')
arrow(ax, f(0, 0), f(4, 0), 'varie', lw=1.5)
arrow(ax, f(0, 0), f(0, 3), 'varie', lw=1.5)
for (x, y), lab, dx, dy in (((0, 0), '(0, 0)', -2, -4), ((4, 0), '(4, 0)', 0, -4), ((0, 3), '(0, 3)', -2, 3.5)):
    disc(ax, f(x, y)[0], f(x, y)[1], 1.0, 'sujet')
    text(ax, f(x, y)[0] + dx, f(x, y)[1] + dy, lab, 'sujet', 's')
text(ax, f(2.9, 2.4)[0], f(2.9, 2.4)[1], 'rectangle : aire 12', 'autre', 's')
text(ax, f(1.1, 0.8)[0] + 4, f(1.1, 0.8)[1], 'terrain', 'sujet', 's')
text(ax, 44, 66, 'terrain : aire 6 = 12 ÷ 2', 'sujet', 'm')
text(ax, 44, 4, 'déterminant 12 : rectangle', 'varie', 's')
save(fig, '38-096')
