import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(80)
x0 = 6; k = 0.5
wa, wb = 92.82 * k, 121.17 * k
for y, unit, va, vb in [(54, 'en mètres', '92,82 m', '121,2 m'), (14, 'en kilomètres', '0,09282 km', '0,1212 km')]:
    text(ax, 6, y + 24, unit, 'encre', 's', ha='left')
    box(ax, x0, y + 14, wa, 7, 'sujet', label=None); text(ax, x0 + 2, y + 17.5, 'côté : ' + va, 'sujet', 's', ha='left')
    arrow(ax, (x0 + 8, y + 13), (x0 + 8, y + 9), 'varie')
    text(ax, x0 + 12, y + 11, r'$\div\,0{,}7660$', 'varie', 's', ha='left')
    box(ax, x0, y + 1, wb, 7, 'resultat', label=None); text(ax, x0 + 2, y + 4.5, 'fraction : ' + vb, 'resultat', 's', ha='left')
line(ax, [(x0 + wa, 2), (x0 + wa, 76)], 'fixe', dash=True)
line(ax, [(x0 + wb, 2), (x0 + wb, 76)], 'fixe', dash=True)
line(ax, [(2, 40), (86, 40)], 'fixe', lw=0.6)
save(fig, '36-037')
