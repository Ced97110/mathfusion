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
box(ax, 4, 54, 22, 11, 'sujet', label='(3, 5)')
text(ax, 31, 59.5, '+', 'encre', 'xl')
box(ax, 36, 54, 22, 11, 'autre', label='(4, 1)')
text(ax, 63, 59.5, '=', 'encre', 'xl')
box(ax, 66, 54, 18, 11, 'resultat', label='(7, 6)')
box(ax, 4, 28, 38, 11, 'varie', label='3 + 4 = 7', size='m')
box(ax, 46, 28, 38, 11, 'varie', label='5 + 1 = 6', size='m')
text(ax, 23, 44, 'premiers nombres', 'varie', 's')
text(ax, 65, 44, 'seconds nombres', 'varie', 's')
trim_arrow(ax, (30, 39), (70, 54), 'varie', 0.3)
trim_arrow(ax, (72, 39), (79, 54), 'varie', 0.3)
text(ax, 44, 17, '(−2) + 3 = 1', 'resultat', 'l')
text(ax, 44, 9, 'on a 7, on doit 6 : 1 de plus', 'resultat', 's')
save(fig, '13-108')
