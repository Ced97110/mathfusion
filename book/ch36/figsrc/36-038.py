import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(64)
cx, cy, u = 44, 33, 8
R = 2.5 * u
A, B, C = [P((cx, cy), R, d) for d in (70, 190, 330)]
ax.add_patch(Circle((cx, cy), 2.5 * u, ec=COL['sujet'], fc=FILL['sujet'], lw=1.6, zorder=1, alpha=0.5))
poly(ax, [A, B, C], 'fixe')
for p, l, d in ((A, 'A', 70), (B, 'B', 190), (C, 'C', 330)):
    disc(ax, p[0], p[1], 1.4, 'sujet')
    q = P((cx, cy), R + 4.5, d); text(ax, q[0], q[1], l, 'sujet', 'l', weight='bold')
text(ax, 44, 60, 'cercle circonscrit', 'sujet', 'm')
text(ax, 44, 3.5, 'il passe par les 3 sommets', 'sujet', 's')
save(fig, '36-038')
