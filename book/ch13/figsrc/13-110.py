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
fig, ax = canvas(84)
P = G(ax, 10, 20, 5, 8)
line(ax, [P(0,2), P(3,5)], 'varie', lw=1.6)
line(ax, [P(1,0), P(5,4)], 'resultat', lw=1.6)
for p in [(1,3),(0,2)]: dpt(ax, P(*p), 'varie', 1.7)
for p in [(5,4),(4,3)]: dpt(ax, P(*p), 'resultat', 1.7)
trim_arrow(ax, P(1,3), P(5,4), 'autre', 2.2)
trim_arrow(ax, P(0,2), P(4,3), 'autre', 2.2)
text(ax, P(1,3)[0]-1, P(1,3)[1]+3.5, '(1, 3)', 'varie', 's', ha='right')
text(ax, P(0,2)[0]+2.6, P(0,2)[1]-3, '(0, 2)', 'varie', 's', ha='left')
text(ax, P(5,4)[0]+3, P(5,4)[1]+1, '(5, 4)', 'resultat', 's', ha='left')
text(ax, P(4,3)[0]+3, P(4,3)[1]-3, '(4, 3)', 'resultat', 's', ha='left')
text(ax, 34, 49, '+ (4, 1)', 'autre', 's')
text(ax, 70, 62, '−2', 'varie', 'l', weight='bold')
text(ax, 70, 56, '+ 3 =', 'autre', 'm')
text(ax, 70, 50, '1', 'resultat', 'l', weight='bold')
text(ax, 44, 7, 'même droite : même résultat', 'resultat', 's')
save(fig, '13-110')
