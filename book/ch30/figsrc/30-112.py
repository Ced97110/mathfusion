import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(72)
X = lambda d: 14 + d * 56 / 90
Y = lambda v: 10 + v * 7
line(ax, [(12, 10), (78, 10)], 'fixe')
for d, s in ((0, '0°'), (45, '45°'), (90, '90°')):
    text(ax, X(d), 6.5, s, 'fixe', 's')
line(ax, [(X(90), 10), (X(90), 62)], 'fixe', dash=True)
dmax = math.degrees(math.atan(6.8 / 2))
curve(ax, lambda d: 2 * math.tan(math.radians(d)), 0, dmax, X, Y, 'sujet')
text(ax, 24, 34, r'$2\,\tan x$', 'sujet', 'm')
for d, s in ((45, '45° : 2'), (60, '60° : 3,46')):
    v = 2 * math.tan(math.radians(d)); disc(ax, X(d), Y(v), 1.2, 'varie')
    text(ax, X(d) - 3, Y(v) + 3.5, s, 'varie', 's', ha='right')
arrow(ax, (X(dmax), Y(6.8)), (X(dmax) + 6, 64), 'sujet')
text(ax, 62, 68, '89,99° : ≈ 11 459', 'sujet', 's', ha='right')
text(ax, 22, 55, 'aucun plus haut point', 'encre', 's')
save(fig, '30-112')
