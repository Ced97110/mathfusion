import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(66)
sc = 0.5; xs = 12
vals = [(r'$\frac{a}{\sin A}$', 'a'), (r'$\frac{b}{\sin B}$', 'b'), (r'$\frac{c}{\sin C}$', 'c')]
ys = [48, 28, 8]
for (lab, _), y in zip(vals, ys):
    box(ax, xs, y, 121.2 * sc, 8, 'resultat', label=None)
    text(ax, 6, y + 4, lab, 'encre', 'm')
    text(ax, xs + 3, y + 4, r'$\approx 121{,}2$', 'resultat', 's', ha='left')
line(ax, [(xs + 121.2 * sc, 6), (xs + 121.2 * sc, 60)], 'fixe', dash=True)
text(ax, 44, 40, r'$=$', 'resultat', 'xl')
text(ax, 44, 20, r'$=$', 'resultat', 'xl')
save(fig, '36-034')
