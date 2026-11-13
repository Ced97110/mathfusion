import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(96)
s = 0.18; b, c = 120, 90
text(ax, 44, 92, r'$a^2=b^2+c^2-2bc\cos A$', 'encre', 'm')
for yb, ang, v, lab in [(66, 50, 92.82, '92,82'), (38, 90, 150, '150'), (10, 130, 190.75, '190,7')]:
    Ap = (20, yb); Bp = (Ap[0] + c * s, yb); Cp = P(Ap, b * s, ang)
    line(ax, [Ap, Bp], 'fixe', lw=1.4)
    line(ax, [Ap, Cp], 'fixe', lw=1.4)
    line(ax, [Bp, Cp], 'varie', lw=1.8)
    arc(ax, Ap, 4, 0, ang, 'encre', 0.8)
    text(ax, 9, yb - 0.5, f'A = {ang}°', 'encre', 's')
    box(ax, 46, yb + 3, v * 0.2, 7, 'varie', label=None)
    text(ax, 48, yb + 6.5, 'a = ' + lab, 'varie', 's', ha='left')
text(ax, 22.5, 77, r'$b$', 'fixe', 's'); text(ax, 28, 62.5, r'$c$', 'fixe', 's')
save(fig, '36-042')
