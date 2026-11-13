import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def G(ax, x0, y0, n, c, xl="j'ai", yl='je dois'):
    for i in range(n + 1):
        for p, q in (((x0 + i*c, y0), (x0 + i*c, y0 + n*c)), ((x0, y0 + i*c), (x0 + n*c, y0 + i*c))):
            ax.plot([p[0], q[0]], [p[1], q[1]], color=COL['fixe'], lw=0.35, alpha=0.45, zorder=1)
    arrow(ax, (x0, y0), (x0 + n*c + 4, y0), 'fixe', lw=0.8)
    arrow(ax, (x0, y0), (x0, y0 + n*c + 4), 'fixe', lw=0.8)
    if xl: text(ax, x0 + n*c + 2, y0 - 3.5, xl, 'fixe', 's')
    if yl: text(ax, x0 + 2, y0 + n*c + 7, yl, 'fixe', 's')
    return lambda a, b: (x0 + a*c, y0 + b*c)
def dpt(ax, p, role, r=1.5):
    disc(ax, p[0], p[1], r, role)
def trim_arrow(ax, p, q, role='varie', t=2.0, curve=0.0, both=False):
    d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
    arrow(ax, (p[0]+ux*t, p[1]+uy*t), (q[0]-ux*t, q[1]-uy*t), role, curve=curve, both=both)
fig, ax = canvas(74)
P = G(ax, 12, 14, 4, 11)
poly(ax, [P(0,0), P(4,0), P(4,4)], 'sujet')
poly(ax, [P(0,0), P(0,4), P(4,4)], 'varie')
line(ax, [P(0,0), P(4,4)], 'encre', lw=1.4)
for p in [(0,0),(1,1),(2,2)]: dpt(ax, P(*p), 'encre', 1.5)
text(ax, P(3,1)[0], P(3,1)[1]+1, 'positifs', 'sujet', 's')
text(ax, P(1,3)[0], P(1,3)[1]+1, 'négatifs', 'varie', 's')
text(ax, P(3,0.4)[0], P(3,0.4)[1]-0.2, 'plus que je dois', 'sujet', 's')
text(ax, P(1,3.4)[0]+3, P(1,3.4)[1]+1.2, 'plus que j’ai', 'varie', 's')
text(ax, P(4,4)[0]+3, P(4,4)[1]+1, '0', 'encre', 'l', ha='left', weight='bold')
text(ax, P(2,2)[0]+3, P(2,2)[1]-2.5, '(2, 2)', 'encre', 's', ha='left')
save(fig, '13-102')
