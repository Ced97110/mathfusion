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
s = 0.3; b = 120
Ap = (5, 12); Cp = P(Ap, b * s, 50); D = (Cp[0], Ap[1])
poly(ax, [Ap, D, Cp], 'fixe')
line(ax, [Ap, Cp], 'sujet', lw=2.0)
line(ax, [Ap, D], 'resultat', lw=2.6)
line(ax, [D, Cp], 'fixe', lw=1.0)
rmark(ax, D, 180, 90, 1.8)
arc(ax, Ap, 6, 0, 50, 'autre', 1.4)
text(ax, Ap[0] + 9.5, Ap[1] + 3, r'$A=50^\circ$', 'autre', 's')
text(ax, 11, 33.5, r'$b=120$', 'sujet', 's')
text(ax, 18, 7, r'$x$', 'resultat', 'm')
text(ax, 18, 2.5, 'adjacent à A', 'resultat', 's')
text(ax, 11, 37.5, 'hypoténuse', 'sujet', 's')
box(ax, 44, 46, 42, 10, 'encre', label=r'$\cos A=\frac{x}{b}$', size='s')
arrow(ax, (65, 45), (65, 39), 'varie'); text(ax, 85, 42, r'$\times\, b$', 'varie', 's', ha='right')
box(ax, 44, 29, 42, 9, 'sujet', label=r'$x=b\cos A$', size='s')
arrow(ax, (65, 28), (65, 22), 'varie')
box(ax, 44, 10, 42, 11, 'resultat', label=r'$x=120\times 0{,}6428\approx 77{,}1$', size='s')
save(fig, '36-046')
