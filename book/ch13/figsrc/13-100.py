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
P = G(ax, 12, 34, 5, 8)
line(ax, [P(2,0), P(5,3)], 'sujet', lw=1.4)
line(ax, [P(0,0), P(5,5)], 'encre', lw=0.8, dash=True)
for p in [(3,1),(4,2)]:
    dpt(ax, P(*p), 'sujet', 1.7)
text(ax, P(3,1)[0]+2.8, P(3,1)[1]-2.8, '(3, 1)', 'sujet', 's', ha='left')
text(ax, P(4,2)[0]+2.8, P(4,2)[1]-2.8, '(4, 2)', 'sujet', 's', ha='left')
text(ax, 58, 60, 'même droite', 'sujet', 's', ha='left')
for p, lab in [((3, 1), "j'ai 3, je dois 1 : +2"), ((4, 2), "j'ai 4, je dois 2 : +2")]:
    q = P(*p)
    line(ax, [(q[0] + 2.2, q[1]), (57, q[1])], 'sujet', lw=0.6, dash=True)
    text(ax, 58, q[1], lab, 'sujet', 's', ha='left')
box(ax, 4, 6, 34, 11, 'sujet', label='3 + 2 = 5', size='m')
box(ax, 50, 6, 34, 11, 'sujet', label='1 + 4 = 5', size='m')
text(ax, 44, 11.5, '=', 'resultat', 'xl')
text(ax, 44, 24, 'même total : équivalents', 'resultat', 's')
save(fig, '13-100')
