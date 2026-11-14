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
PL = G(ax, 8, 28, 4, 8, xl=None, yl=None)
PR = G(ax, 50, 28, 4, 8, xl=None, yl=None)
dpt(ax, PL(1,3), 'sujet', 2.0)
line(ax, [PR(0,2), PR(2,4)], 'varie', lw=1.8)
dpt(ax, PR(1,3), 'sujet', 2.0)
text(ax, 24, 69, 'sans barre', 'sujet', 's')
text(ax, 66, 69, 'avec barre', 'varie', 's')
text(ax, 24, 64, r'$(1,3)$', 'sujet', 'm')
text(ax, 66, 64, r'$(1,\overline{3})$', 'varie', 'm')
text(ax, 24, 21, 'un seul point', 'sujet', 's')
text(ax, 66, 21, 'toute la droite', 'varie', 's')
text(ax, 44, 9, r'$(1,\overline{3}) = (0,\overline{2})$', 'varie', 'l')
text(ax, 44, 3.5, 'deux couples, une droite', 'varie', 's')
save(fig, '13-105')
