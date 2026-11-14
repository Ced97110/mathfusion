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
a, b, c, Bd = 92.82, 120, 90, 82.03
s = 0.4
Bp = (6, 10); Cp = (Bp[0] + a * s, Bp[1]); Ap = P(Bp, c * s, Bd); E = (Ap[0], Bp[1])
poly(ax, [Bp, Cp, Ap], 'fixe')
line(ax, [Bp, Ap], 'sujet', lw=1.6)
line(ax, [Cp, Ap], 'autre', lw=1.6)
line(ax, [Bp, Cp], 'fixe', lw=1.0)
line(ax, [E, Ap], 'resultat', lw=2.0)
rmark(ax, E, 0, 90, 2.0)
text(ax, 5, 33, r'$c$', 'sujet', 'm'); text(ax, 30, 32, r'$b$', 'autre', 'm')
text(ax, E[0] - 3.2, 28, r'$h$', 'resultat', 'm')
text(ax, Ap[0] + 1, Ap[1] + 4, r'$A$', 'fixe', 's')
text(ax, Bp[0] - 1.5, Bp[1] - 3, r'$B$', 'sujet', 's'); text(ax, Cp[0] + 1.5, Cp[1] - 3, r'$C$', 'autre', 's')
box(ax, 46, 47, 40, 12, 'sujet', label=r'$c\sin B=90\times\sin 82{,}03^\circ$' + '\n' + r'$\approx 89{,}13$', size='s')
box(ax, 46, 25, 40, 12, 'autre', label=r'$b\sin C=120\times\sin 47{,}97^\circ$' + '\n' + r'$\approx 89{,}13$', size='s')
text(ax, 66, 42, r'$=$', 'resultat', 'xl')
arrow(ax, (66, 24), (66, 17), 'varie')
text(ax, 66, 13, r'$\frac{b}{\sin B}=\frac{c}{\sin C}$', 'resultat', 'l')
text(ax, 80, 20.5, r'$\div\sin B\,\sin C$', 'varie', 's', ha='right')
save(fig, '36-028')
