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
fig, ax = canvas(92)
P = G(ax, 12, 40, 4, 9)
line(ax, [P(0,2), P(2,4)], 'varie', lw=1.4)
dpt(ax, P(1,3), 'varie', 1.9)
line(ax, [P(1,1), P(1,3)], 'varie', lw=0.9, dash=True)
text(ax, P(1,3)[0]+3, P(1,3)[1]-3, '(1, 3)', 'varie', 's', ha='left')
text(ax, P(1,2)[0]+2, P(1,2)[1]-1, 'écart 2', 'varie', 's', ha='left')
text(ax, 56, 62, "j'ai 1, je dois 3", 'varie', 's', ha='left')
f = numberline(ax, 12, 64, 14, -4, 2, arrow_right=False, every=2, role='fixe')
dpt(ax, (f(-2), 14), 'varie', 2.0)
trim_arrow(ax, (P(1,3)[0], P(1,1)[1]-1), (f(-2), 18), 'varie', 0.5, curve=0.0)
text(ax, f(-2), 7, '−2', 'varie', 'l', weight='bold')
text(ax, 72, 14, 'situation −2', 'varie', 's')
save(fig, '13-101')
