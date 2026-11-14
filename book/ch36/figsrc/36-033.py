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
s = 0.4
Ap = (6, 8); Bp = (Ap[0] + 90 * s, Ap[1]); Cp = P(Ap, 120 * s, 50)
poly(ax, [Ap, Bp, Cp], 'fixe')
line(ax, [Ap, Cp], 'fixe', lw=1.2); line(ax, [Ap, Bp], 'fixe', lw=1.2)
line(ax, [Bp, Cp], 'sujet', lw=2.0)
arc(ax, Ap, 7, 0, 50, 'autre', 1.6)
text(ax, 46, 27, r'$a$', 'sujet', 'm')
text(ax, Ap[0] + 12.5, Ap[1] + 3.2, r'$A$', 'autre', 'm')
text(ax, 66, 58, r'$a=92{,}82$', 'sujet', 'm')
line(ax, [(52, 52), (82, 52)], 'encre', lw=1.0)
text(ax, 67, 46, r'$\sin A=0{,}7660$', 'autre', 'm')
text(ax, 67, 38, r'$=$', 'resultat', 'xl')
text(ax, 67, 28, r'$\approx 121{,}2$', 'resultat', 'l')
text(ax, 67, 15, 'côté ÷ sinus de', 'encre', 's'); text(ax, 67, 11, 'l’angle en face', 'encre', 's')
save(fig, '36-033')
