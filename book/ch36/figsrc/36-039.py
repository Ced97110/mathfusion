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
cx, cy, u = 25, 33, 6
C = (cx - 2 * u, cy - 1.5 * u); A = (cx - 2 * u, cy + 1.5 * u); B = (cx + 2 * u, cy - 1.5 * u)
ax.add_patch(Circle((cx, cy), 2.5 * u, ec=COL['sujet'], fc=FILL['sujet'], lw=1.4, zorder=1, alpha=0.5))
poly(ax, [A, B, C], 'fixe')
rmark(ax, C, 0, 90, 2.0)
line(ax, [(cx, cy), A], 'varie', lw=1.6)
disc(ax, cx, cy, 0.9, 'varie')
text(ax, cx - 3.5, cy + 10.5, r'$R=2{,}5$', 'varie', 's')
text(ax, cx + 5, cy - 2.5, r'$2R=5$', 'resultat', 's')
text(ax, C[0] + 3.5, cy, r'$3$', 'encre', 's'); text(ax, cx - 3, C[1] + 3.5, r'$4$', 'encre', 's')
text(ax, 66, 60, r'$\frac{a}{\sin A}=2R$', 'encre', 'l')
for y, t in [(47, r'$3\div 0{,}6=5$'), (35, r'$4\div 0{,}8=5$'), (23, r'$5\div 1=5$')]:
    box(ax, 50, y - 4.5, 34, 9, 'resultat', label=t, size='s')
text(ax, 66, 12, 'les trois valent le', 'resultat', 's'); text(ax, 66, 8, 'diamètre du cercle', 'resultat', 's')
save(fig, '36-039')
