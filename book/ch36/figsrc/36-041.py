import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(60)
u = 7
Ap = (5, 12); Cp = (Ap[0] + 4 * u, Ap[1]); Bp = (Cp[0], Ap[1] + 3 * u)
poly(ax, [Ap, Cp, Bp], 'fixe')
line(ax, [Ap, Bp], 'sujet', lw=2.0); line(ax, [Cp, Bp], 'sujet', lw=2.0)
line(ax, [Ap, Cp], 'fixe', lw=1.2)
rmark(ax, Cp, 180, 90, 2.4)
arc(ax, Ap, 7, 0, math.degrees(math.atan2(3, 4)), 'autre', 1.4)
text(ax, Ap[0] + 11, Ap[1] + 2.5, r'$A$', 'autre', 's')
text(ax, Cp[0] - 3.5, Cp[1] + 3.5, r'$C=90^\circ$', 'encre', 's', ha='right')
text(ax, Cp[0] + 4, (Cp[1] + Bp[1]) / 2, r'$a=3$', 'sujet', 's')
text(ax, 14, 34, r'$c=5$', 'sujet', 's')
box(ax, 47, 47, 38, 9, 'encre', label=r'$\sin C=1$', size='s')
arrow(ax, (66, 46), (66, 40), 'varie')
box(ax, 47, 31, 38, 9, 'sujet', label=r'$\frac{3}{\sin A}=\frac{5}{1}=5$', size='s')
arrow(ax, (66, 30), (66, 24), 'varie')
box(ax, 47, 12, 38, 12, 'resultat', label=r'$\sin A=\frac{3}{5}=0{,}6$', size='s')
save(fig, '36-041')
