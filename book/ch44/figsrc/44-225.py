import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(48)
xs = (14, 44, 74); st = ([1, 2, 3], [1, 3, 2], [1, 2, 3]); rl = ('sujet', 'varie', 'resultat')
for i, cx in enumerate(xs):
    poly(ax, pg(cx, 22, 10, 3), rl[i])
    line(ax, [(cx, 22 + 14), (cx, 22 - 8)], 'fixe', dash=True)
    for k, ang in enumerate((90, 210, 330)):
        x, y = pol(cx, 22, 5.5, ang); text(ax, x, y - (1 if k == 0 else 0), str(st[i][k]), rl[i], 's')
for i in range(2):
    arrow(ax, (xs[i] + 13, 24), (xs[i + 1] - 13, 24), 'varie', curve=-0.0)
    text(ax, (xs[i] + xs[i + 1]) / 2, 28, r'$s$', 'varie', 'm')
text(ax, 44, 42, 'même axe deux fois', 'fixe', 'm')
text(ax, 44, 4, r'$s^2 = 1$', 'resultat', 'l')
save(fig, '44-225')
