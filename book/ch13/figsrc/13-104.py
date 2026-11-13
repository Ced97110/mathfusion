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
fig, ax = canvas(78)
P = G(ax, 12, 20, 5, 8)
line(ax, [P(0,2), P(3,5)], 'varie', lw=1.8)
pts = [(0,2),(1,3),(2,4),(3,5)]
for p in pts:
    dpt(ax, P(*p), 'varie', 1.7)
    text(ax, P(*p)[0]+2.8, P(*p)[1]-2.8, f'({p[0]}, {p[1]})', 'varie', 's', ha='left')
text(ax, P(3,5)[0]+3, P(3,5)[1]+2.5, '…(10, 12)', 'varie', 's', ha='left')
box(ax, 58, 28, 26, 14, 'resultat', label='−2', size='l', weight='bold')
text(ax, 71, 22, 'un seul nombre', 'resultat', 's')
text(ax, 71, 46, 'toute la droite', 'resultat', 's')
trim_arrow(ax, P(2,3.2), (58, 38), 'resultat', 0.5)
save(fig, '13-104')
