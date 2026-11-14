import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(55)
text(ax, 44, 49, r'3 rotations : $3=3^1$', 'autre', 'l')
R = 8.0
def tri(cx, cy):
    return [(cx + R * math.cos(math.radians(90 + 120 * k)), cy + R * math.sin(math.radians(90 + 120 * k))) for k in range(3)]
labs = [('e', 'ne rien faire'), ('r', '1/3 de tour'), (r'$r^2$', '2/3 de tour')]
xs = [16, 44, 72]
for i, x in enumerate(xs):
    pts = tri(x, 30)
    poly(ax, pts, 'autre')
    disc(ax, pts[i][0], pts[i][1], 1.6, 'varie')
    text(ax, x, 15, labs[i][0], 'autre', 'l')
    text(ax, x, 9, labs[i][1], 'encre', 's')
for i in range(2):
    arrow(ax, (xs[i] + 11, 30), (xs[i + 1] - 11, 30), 'varie')
    text(ax, (xs[i] + xs[i + 1]) / 2, 34, r'$\times r$', 'varie', 's')
save(fig, '50-024')
