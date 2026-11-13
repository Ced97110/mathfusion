import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(106)
s = 0.38; b, c = 120, 90
x = b * cs(50)
def panel(yb, Ax, ang):
    Ap = (Ax, yb); Bp = (Ax + c * s, yb); Cp = P(Ap, b * s, ang); D = (Cp[0], yb)
    poly(ax, [Ap, Bp, Cp], 'fixe')
    line(ax, [Ap, Bp], 'fixe', lw=1.2)
    line(ax, [Ap, Cp], 'sujet', lw=1.6)
    line(ax, [D, Cp], 'fixe', lw=1.0, dash=True)
    if ang > 90: line(ax, [D, Ap], 'fixe', lw=1.0, dash=True)
    line(ax, [Ap, D], 'resultat', lw=2.6)
    rmark(ax, D, 0 if ang < 90 else 0, 90, 1.8)
    return Ap, Bp, Cp, D
Ap, Bp, Cp, D = panel(64, 18, 50)
arc(ax, Ap, 5, 0, 50, 'encre', 0.8)
text(ax, Ap[0] + 9, Ap[1] + 3.2, r'$A=50^\circ$', 'encre', 's')
text(ax, Ap[0] + 7.5, 59.5, r'$x=77{,}13$', 'resultat', 's')
brace(ax, D[0], Bp[0], 62.5, 'autre', label=r'$c-x=12{,}87$', depth=1.4)
text(ax, D[0] - 2.5, 67.5, r'$D$', 'fixe', 's'); text(ax, Bp[0] + 2.5, 67.5, r'$B$', 'fixe', 's')
text(ax, Ap[0] + 5, 82, r'$b=120$', 'sujet', 's')
Ap, Bp, Cp, D = panel(20, 40, 130)
arc(ax, Ap, 5, 0, 130, 'encre', 0.8)
text(ax, Ap[0] + 7, Ap[1] + 5.5, r'$A=130^\circ$', 'encre', 's')
text(ax, (D[0] + Ap[0]) / 2, 15.5, r'$x=-77{,}13$', 'resultat', 's')
brace(ax, D[0], Bp[0], 12.5, 'autre', label=r'$c+x=167{,}13$', depth=1.4)
text(ax, D[0] + 3.5, 23.5, r'$D$', 'fixe', 's'); text(ax, Bp[0] + 2.5, 23.5, r'$B$', 'fixe', 's')
text(ax, Ap[0] - 8, 36, r'$b=120$', 'sujet', 's')
save(fig, '36-044')
