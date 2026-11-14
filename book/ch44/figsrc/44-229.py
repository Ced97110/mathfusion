import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(62)
def sq(cx, cy, p1, p2):
    poly(ax, pg(cx, cy, 7, 4, 45), 'fixe')
    x, y = pol(cx, cy, 7, 45 + 90 * (p1 % 4)); disc(ax, x, y, 2.0, 'sujet')
    x, y = pol(cx, cy, 7, 45 + 90 * (p2 % 4)); disc(ax, x, y, 2.0, 'varie')
xs = [11 + 22 * k for k in range(4)]
rot = ('1', r'$r$', r'$r^2$', r'$r^3$'); ref = (r'$s$', r'$rs$', r'$r^2s$', r'$r^3s$')
for k, cx in enumerate(xs):
    sq(cx, 40, k, k + 1); text(ax, cx, 28.5, rot[k], 'sujet', 'm')
    sq(cx, 14, 3 + k, 2 + k); text(ax, cx, 2.5, ref[k], 'varie', 'm')
text(ax, 44, 57, '4 rotations : même ordre', 'sujet', 's')
text(ax, 44, 22, '4 réflexions : ordre inversé', 'varie', 's')
disc(ax, 4, 60.5, 1.4, 'sujet'); text(ax, 7, 60.5, 'sommet 1', 'sujet', 's', ha='left')
disc(ax, 63, 60.5, 1.4, 'varie'); text(ax, 66, 60.5, 'sommet 2', 'varie', 's', ha='left')
save(fig, '44-229')
