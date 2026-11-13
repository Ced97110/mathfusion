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
s = 0.36; b, c = 120, 90
Ap = (3, 10); Bp = (Ap[0] + c * s, Ap[1]); Cp = P(Ap, b * s, 50); D = (Cp[0], Ap[1])
poly(ax, [Ap, D, Cp], 'sujet'); poly(ax, [D, Bp, Cp], 'autre')
line(ax, [Ap, Bp], 'fixe', lw=1.0)
line(ax, [D, Cp], 'resultat', lw=2.0)
rmark(ax, D, 180, 90, 1.8); rmark(ax, D, 0, 90, 1.8)
text(ax, Ap[0] + 10, 34, r'$b$', 'sujet', 's'); text(ax, D[0] + 6.5, 34, r'$a$', 'autre', 's')
text(ax, D[0] - 3, 22, r'$h$', 'resultat', 's')
text(ax, Ap[0] + 6, 5.5, r'$x$', 'sujet', 's'); text(ax, D[0] + 2.5, 5.5, r'$c-x$', 'autre', 's')
text(ax, Cp[0], Cp[1] + 3, r'$C$', 'fixe', 's')
box(ax, 42, 52, 44, 11, 'autre', label=r'$a^2=h^2+(c-x)^2$' + '\n' + r'$8\,615{,}8\approx 8\,450{,}3+165{,}5$', size='s')
arrow(ax, (64, 51), (64, 44), 'varie')
text(ax, 85, 47.5, r'remplacer $h^2$', 'varie', 's', ha='right')
box(ax, 42, 33, 44, 10, 'sujet', label=r'$h^2=b^2-x^2$', size='s')
arrow(ax, (64, 32), (64, 25), 'varie')
box(ax, 42, 12, 44, 12, 'resultat', label=r'$a^2=b^2+c^2-2bc\cos A$', size='s')
save(fig, '36-043')
