import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 14, 58, 8, 0, 2, arrow_right=False)
text(ax, 70, 8, r'$x$', 'fixe', 'm')
g = lambda v: 14 + 6 * v
pts = [(f(k), g(2 * k + 1)) for k in range(3)]
for k in range(2):
    (xa, ya), (xb, yb) = pts[k], pts[k + 1]
    line(ax, [(xa, ya), (xb, ya)], 'fixe', lw=1.2)
    line(ax, [(xb, ya), (xb, yb)], 'varie', lw=1.4)
line(ax, [pts[0], pts[2]], 'sujet', dash=True)
for (x, y), v in zip(pts, ('1', '3', '5')):
    disc(ax, x, y, 1.3, 'sujet')
    text(ax, x - 4, y + 1, v, 'sujet', 'm', ha='right')
text(ax, 51, 24, r'$x$ : $+1$', 'fixe', 's')
text(ax, 71, 36, r'valeur : $+2$', 'varie', 's')
text(ax, 44, 59, r'$2x+1$', 'sujet', 'l')
text(ax, 72, 48, r'$a = 2$', 'varie', 'l')
save(fig, '15-137')
