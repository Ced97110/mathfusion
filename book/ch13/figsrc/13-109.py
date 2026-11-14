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
text(ax, 15, 73, 'même droite', 'sujet', 's')
text(ax, 71, 73, 'même droite ?', 'resultat', 's')
box(ax, 4, 56, 22, 10, 'sujet', label='(1, 3)')
box(ax, 4, 38, 22, 10, 'sujet', label='(2, 4)')
text(ax, 15, 51.5, '∼', 'sujet', 'l')
for y, a, b in ((56, '(6, 3)', '+ (5, 0)'), (38, '(7, 4)', '+ (5, 0)')):
    arrow(ax, (27, y+5), (59, y+5), 'varie')
    text(ax, 43, y+8.5, b, 'varie', 's')
    box(ax, 60, y, 24, 10, 'resultat', label=a)
text(ax, 72, 51.5, '∼ ?', 'resultat', 'l')
box(ax, 22, 6, 62, 18, 'resultat', fill=True)
text(ax, 53, 18, '6 + 4 = 10 et 3 + 7 = 10', 'resultat', 'm', weight='bold')
text(ax, 53, 11, 'totaux égaux : (6, 3) ∼ (7, 4)', 'resultat', 's')
trim_arrow(ax, (72, 24), (72, 36), 'resultat', 0.3)
save(fig, '13-109')
