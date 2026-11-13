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
P = G(ax, 12, 24, 5, 8)
line(ax, [P(0,0), P(5,5)], 'fixe', lw=1.2, dash=True)
dpt(ax, P(3,5), 'varie', 2.0); dpt(ax, P(5,3), 'sujet', 2.0)
trim_arrow(ax, P(3,5), P(5,3), 'encre', 2.6, both=True)
text(ax, P(3,5)[0]-3, P(3,5)[1]+1, '(3, 5)', 'varie', 's', ha='right')
text(ax, P(5,3)[0]+3, P(5,3)[1]-3, '(5, 3)', 'sujet', 's', ha='left')
text(ax, P(3,5)[0]-3, P(3,5)[1]-3.5, 'j’ai 3, je dois 5', 'varie', 's', ha='right')
text(ax, P(5,3)[0]+3, P(5,3)[1]-7, 'j’ai 5, je dois 3', 'sujet', 's', ha='left')
text(ax, 70, 52, 'échange', 'encre', 's')
text(ax, P(5,5)[0]+3, P(5,5)[1]+1, '0', 'fixe', 'l', ha='left', weight='bold')
text(ax, 44, 8, '(3, 5) + (5, 3) = (8, 8)', 'resultat', 'm')
save(fig, '13-111')
