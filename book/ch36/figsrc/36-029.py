import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(74)
u = 4.6
Ap = (44, 28); Bp = (Ap[0] + 7 * u, Ap[1]); Cp = P(Ap, 10 * u, 130); D = (Cp[0], Ap[1])
poly(ax, [Ap, Bp, Cp], 'fixe')
line(ax, [Ap, D], 'fixe', lw=1.0, dash=True)
line(ax, [Ap, Cp], 'sujet', lw=1.6)
line(ax, [D, Cp], 'resultat', lw=2.0)
rmark(ax, D, 0, 90, 2.0)
arc(ax, Ap, 6, 0, 130, 'encre')
arc(ax, Ap, 9, 130, 180, 'varie')
text(ax, Ap[0] + 6, Ap[1] + 8, r'$130^\circ$', 'encre', 's')
text(ax, Ap[0] - 12, Ap[1] + 3.5, r'$50^\circ$', 'varie', 's')
text(ax, Ap[0] + 2, Ap[1] - 3.5, r'$A$', 'fixe', 's')
text(ax, D[0] - 2, D[1] - 3, r'$D$', 'fixe', 's')
text(ax, (Ap[0] + Cp[0]) / 2 + 3, (Ap[1] + Cp[1]) / 2 + 3, r'$b=10$', 'sujet', 's')
text(ax, D[0] - 4.5, (D[1] + Cp[1]) / 2, r'$h$', 'resultat', 'm')
box(ax, 4, 14, 80, 9, 'resultat', label=r'$\sin 130^\circ=\sin 50^\circ\approx 0{,}7660$', size='s')
box(ax, 4, 3, 80, 9, 'resultat', label=r'$h=10\times 0{,}7660\approx 7{,}66$', size='s')
save(fig, '36-029')
