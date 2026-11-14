import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(72)
s = 0.6
Ap = (12, 8); Bp = (Ap[0] + 90 * s, Ap[1]); Cp = P(Ap, 120 * s, 50)
poly(ax, [Ap, Bp, Cp], 'fixe')
line(ax, [Bp, Cp], 'sujet', lw=2.0)
line(ax, [Cp, Ap], 'sujet', lw=2.0)
line(ax, [Ap, Bp], 'sujet', lw=2.0)
text(ax, 74, 36, r'$a=92{,}82$', 'sujet', 'm')
text(ax, 20, 44, r'$b=120$', 'sujet', 'm')
text(ax, 38, 3, r'$c=90$', 'sujet', 'm')
text(ax, Ap[0] - 2, Ap[1] - 2.5, r'$A$', 'fixe', 's')
text(ax, Bp[0] + 2, Bp[1] - 2.5, r'$B$', 'fixe', 's')
text(ax, Cp[0] + 1, Cp[1] + 3.5, r'$C$', 'fixe', 's')
save(fig, '36-030')
