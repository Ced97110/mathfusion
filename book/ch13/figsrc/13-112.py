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
fig, ax = canvas(80)
box(ax, 4, 50, 22, 11, 'sujet', label='(3, 1)')
text(ax, 31, 55.5, '×', 'encre', 'xl')
box(ax, 36, 50, 22, 11, 'autre', label='(2, 5)')
text(ax, 63, 55.5, '=', 'encre', 'xl')
box(ax, 66, 50, 18, 11, 'resultat', label='(11, 17)', size='s')
text(ax, 15, 66, 'vaut 2', 'sujet', 's')
text(ax, 47, 66, 'vaut −3', 'autre', 's')
text(ax, 75, 66, 'vaut −6', 'resultat', 's')
box(ax, 4, 20, 38, 12, 'varie', label='3×2 + 1×5 = 11', size='s')
box(ax, 46, 20, 38, 12, 'varie', label='3×5 + 1×2 = 17', size='s')
trim_arrow(ax, (30, 32), (70, 50), 'varie', 0.3)
trim_arrow(ax, (72, 32), (78, 50), 'varie', 0.3)
text(ax, 23, 14, 'première place', 'varie', 's')
text(ax, 65, 14, 'seconde place', 'varie', 's')
text(ax, 44, 6, '2 × (−3) = −6', 'resultat', 'm')
save(fig, '13-112')
