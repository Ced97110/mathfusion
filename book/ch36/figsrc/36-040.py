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
cx, cy, u = 25, 28, 6
Bp = (cx - 2.5 * u, cy); Cp = (cx + 2.5 * u, cy); Ap = (Bp[0] + 1.8 * u, cy + 2.4 * u)
ax.add_patch(Circle((cx, cy), 2.5 * u, ec=COL['sujet'], fc=FILL['sujet'], lw=1.4, zorder=1, alpha=0.5))
poly(ax, [Ap, Bp, Cp], 'fixe')
line(ax, [Bp, Cp], 'resultat', lw=2.4)
d1 = math.degrees(math.atan2(Bp[1] - Ap[1], Bp[0] - Ap[0])); d2 = math.degrees(math.atan2(Cp[1] - Ap[1], Cp[0] - Ap[0]))
rmark(ax, Ap, d1, d2, 2.4, 'autre')
text(ax, Ap[0] + 2, Ap[1] + 4, r'$A=90^\circ$', 'autre', 's')
text(ax, cx, cy + 4, r'$a=5$', 'sujet', 's')
arrow(ax, (Bp[0], cy - 17), (Cp[0], cy - 17), 'resultat', both=True)
text(ax, cx, cy - 21, 'diamètre = 5', 'resultat', 's')
text(ax, 67, 48, r'$\sin A=1$', 'autre', 'm')
text(ax, 67, 36, r'$\frac{a}{\sin A}=5\div 1$', 'encre', 'm')
text(ax, 67, 25, r'$=5$', 'resultat', 'l')
save(fig, '36-040')
