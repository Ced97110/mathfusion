import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, s = 5, 8, 7.0
P = lambda x, y: (ox + x * s, oy + y * s)
cls = [(0, 'sujet', (2, 1)), (1, 'varie', (1, 0)), (-1, 'autre', (1, 1))]
for x in range(7):
    for y in range(4):
        disc(ax, P(x, y)[0], P(x, y)[1], 0.9, 'fixe', fill=False)
for c, r, pt in cls:
    x0 = max(0, c); x1 = min(6, 6 + c)
    line(ax, [P(x0, (x0 - c) / 2), P(x1, (x1 - c) / 2)], r, lw=1.1)
    disc(ax, P(*pt)[0], P(*pt)[1], 2.0, r)
box(ax, 54, 34, 30, 9, 'autre', label='(1 ; 1) : 1 − 2 = −1', size='s')
box(ax, 54, 21, 30, 9, 'varie', label='(1 ; 0) : 1 − 0 = 1', size='s')
box(ax, 54, 8, 30, 9, 'sujet', label='(2 ; 1) : 2 − 2 = 0', size='s')
text(ax, 69, 47, 'repère = x − 2y', 'encre', 's')
save(fig, '57-188')
