import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(58)
R = 22
text(ax, 28, 54, 'bleu : hypoténuse = 1', 'sujet', 's'); text(ax, 70, 54, 'vert : sinus', 'resultat', 's')
for x0, ang, val in [(4, 30, '0,5'), (33, 50, '0,7660'), (62, 90, '1')]:
    y0 = 18
    V = (x0, y0); T = P(V, R, ang); F = (T[0], y0)
    line(ax, [V, F], 'fixe', lw=1.0)
    line(ax, [F, T], 'resultat', lw=3.2)
    line(ax, [V, T], 'sujet', lw=1.4)
    if ang < 90: rmark(ax, F, 180, 90, 1.8)
    else: rmark(ax, V, 0, 90, 1.8)
    arc(ax, V, 6, 0, ang, 'varie', 1.0)
    text(ax, x0 + 9.5 if ang < 90 else x0 + 5, y0 + (2.5 if ang == 30 else 4.5 if ang == 50 else 11), f'{ang}°', 'varie', 's')
    text(ax, x0 + 9, 12, f'sin {ang}°', 'encre', 's')
    text(ax, x0 + 9, 6.5, f'= {val}', 'resultat', 's')
save(fig, '36-032')
