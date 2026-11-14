import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(52)
for cx in (22, 66):
    poly(ax, pg(cx, 26, 11, 4, 45), 'sujet')
    for k in range(4):
        x, y = pol(cx, 26, 7, 45 + 90 * k); text(ax, x, y, str(k + 1), 'sujet', 's')
a = 4.5
arrow(ax, pol(22, 26, 11 + a, 62), pol(22, 26, 11 + a, 118), 'varie', curve=0.3)
line(ax, [(66 - 17, 26), (66 + 17, 26)], 'varie', dash=True)
arrow(ax, (66 + 12.5, 26 + 5.5), (66 + 12.5, 26 - 5.5), 'varie', both=True)
text(ax, 22, 8, r'$r$ : rotation', 'varie', 'l'); text(ax, 22, 2.5, '360°/$n$ = 90°', 'varie', 's')
text(ax, 66, 8, r'$s$ : réflexion', 'varie', 'l'); text(ax, 66, 2.5, 'autour d’un axe', 'varie', 's')
save(fig, '44-223')
