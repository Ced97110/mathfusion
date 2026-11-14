import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(62)
s = 0.2; b = 120
Ap = (5, 36); Cp = P(Ap, b * s, 50); D = (Cp[0], Ap[1])
poly(ax, [Ap, D, Cp], 'fixe')
line(ax, [Ap, Cp], 'sujet', lw=1.8); line(ax, [Ap, D], 'autre', lw=1.8); line(ax, [D, Cp], 'resultat', lw=1.8)
rmark(ax, D, 180, 90, 1.6)
text(ax, 9, 49, r'$b$', 'sujet', 's'); text(ax, 13, 32, r'$x$', 'autre', 's'); text(ax, D[0] + 3, 44.5, r'$h$', 'resultat', 's')
text(ax, 62, 47, r'$h^2=b^2-x^2$', 'encre', 'l')
k = 76 / 14400
box(ax, 6, 20, 14400 * k, 7, 'sujet', label=None); text(ax, 8, 23.5, r'$b^2=14\,400$', 'sujet', 's', ha='left')
box(ax, 6, 10, 5949.7 * k, 7, 'autre', label=None); text(ax, 8, 13.5, r'$x^2=5\,949{,}7$', 'autre', 's', ha='left')
box(ax, 6 + 5949.7 * k, 10, 8450.3 * k, 7, 'resultat', label=None); text(ax, 8 + 5949.7 * k, 13.5, r'$h^2=8\,450{,}3$', 'resultat', 's', ha='left')
save(fig, '36-047')
