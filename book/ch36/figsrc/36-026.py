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
b, c, A = 120, 90, 50
s = 0.38
Ap = (4, 8); Bp = (Ap[0] + c * s, Ap[1]); Cp = P(Ap, b * s, A); D = (Cp[0], Ap[1])
poly(ax, [Ap, Bp, Cp], 'fixe')
line(ax, [Ap, Cp], 'sujet', lw=1.6)
line(ax, [Bp, Cp], 'autre', lw=1.6)
line(ax, [Ap, Bp], 'fixe', lw=1.0)
line(ax, [D, Cp], 'resultat', lw=2.0)
rmark(ax, D, 180, 90, 2.0)
text(ax, 17, 33, r'$b$', 'sujet', 'm'); text(ax, 40, 31, r'$a$', 'autre', 'm')
text(ax, D[0] - 3, 25, r'$h$', 'resultat', 'm')
text(ax, 11, 12, r'$A$', 'sujet', 's')
text(ax, Bp[0] + 2.5, Ap[1] - 1, r'$B$', 'autre', 's')
box(ax, 48, 34, 38, 13, 'sujet', label=r'$b\sin A=120\times\sin 50^\circ$' + '\n' + r'$\approx 91{,}92$', size='s')
box(ax, 48, 9, 38, 13, 'autre', label=r'$a\sin B=92{,}82\times\sin 82{,}03^\circ$' + '\n' + r'$\approx 91{,}92$', size='s')
text(ax, 67, 28, r'$=$', 'resultat', 'xl')
save(fig, '36-026')
