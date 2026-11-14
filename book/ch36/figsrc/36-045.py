import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(76)
s = 0.6; b, c = 120, 90
Ap = (8, 14); Bp = (Ap[0] + c * s, Ap[1]); Cp = P(Ap, b * s, 50); D = (Cp[0], Ap[1])
poly(ax, [Ap, D, Cp], 'fixe')
line(ax, [D, Bp], 'fixe', lw=1.0)
line(ax, [Ap, Cp], 'fixe', lw=1.6)
line(ax, [D, Cp], 'varie', lw=2.0)
line(ax, [Ap, D], 'sujet', lw=3.0)
rmark(ax, D, 180, 90, 2.2)
text(ax, 24, 47, r'$b=120$', 'fixe', 's')
text(ax, D[0] - 10, 38.5, r'$h=91{,}92$', 'varie', 's')
text(ax, 31, 8.5, r'$x=77{,}13$', 'sujet', 'm')
text(ax, Bp[0] - 4, 8.5, r'$c=90$', 'fixe', 's', ha='left')
text(ax, Ap[0] - 1, Ap[1] - 3.5, r'$A$', 'fixe', 's')
text(ax, 31, 3.5, 'le long de c', 'sujet', 's'); text(ax, D[0] - 10, 34, 'à angle droit de c', 'varie', 's')
save(fig, '36-045')
