import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(70)
s = 0.4; h, r = 91.925, 12.865
D = (8, 10); Bp = (D[0] + r * s, D[1]); Cp = (D[0], D[1] + h * s)
poly(ax, [D, Bp, Cp], 'autre')
line(ax, [Cp, Bp], 'sujet', lw=2.0); line(ax, [D, Cp], 'resultat', lw=2.0); line(ax, [D, Bp], 'varie', lw=2.4)
rmark(ax, D, 0, 90, 1.6)
text(ax, D[0] - 4, 30, r'$h$', 'resultat', 's')
text(ax, Bp[0] + 3.5, 28, r'$a$', 'sujet', 's')
text(ax, D[0] + 3, 5.5, r'$c-x$', 'varie', 's')
steps = [(r'$c-x=90-77{,}13=12{,}87$', 'varie', 55), (r'$h^2\approx 8\,450{,}3\;;\;(c-x)^2\approx 165{,}5$', 'autre', 40),
         (r'$a^2\approx 8\,450{,}3+165{,}5=8\,615{,}8$', 'sujet', 25), (r'$a\approx 92{,}82$', 'resultat', 10)]
for t, role, y in steps:
    box(ax, 22, y, 64, 9, role, label=t, size='s')
for y in (55, 40, 25): arrow(ax, (54, y), (54, y - 6), 'fixe')
save(fig, '36-048')
