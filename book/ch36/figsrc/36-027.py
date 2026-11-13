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
x0, x1, y0, H = 8, 76, 24, 30
f = lambda v: x0 + v / 180 * (x1 - x0)
line(ax, [(x0, y0), (x1, y0)], 'fixe')
pts = [(i * 2, f(i * 2), y0 + H * sn(i * 2)) for i in range(1, 90)]
line(ax, [(p[1], p[2]) for p in pts], 'fixe', lw=1.0)
for ang, role, name, val in [(50, 'sujet', r'$A=50^\circ$', '0,7660'), (82.03, 'autre', r'$B=82{,}03^\circ$', '0,9903')]:
    px, py = f(ang), y0 + H * sn(ang)
    line(ax, [(px, y0), (px, py)], role, lw=1.0, dash=True)
    disc(ax, px, py, 1.1, role)
    text(ax, px + (-6 if ang == 50 else 6), py + 3.5, val, role, 's')
    text(ax, px, y0 - 4, name, role, 's')
for xe in (x0, x1):
    disc(ax, xe, y0, 1.3, 'limite', fill=False, lw=1.0)
text(ax, x0 - 2, y0 - 4, '0° exclu', 'limite', 's', ha='left')
text(ax, x1 + 2, y0 - 4, '180° exclu', 'limite', 's', ha='right')
text(ax, 44, 67, 'sinus de l’angle, de 0° à 180°', 'encre', 'm')
box(ax, 8, 3, 72, 9, 'resultat', label=r'$0{,}7660\times 0{,}9903\approx 0{,}7586\;>\;0$', size='s')
save(fig, '36-027')
