import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
def P(cx, cy, R, a): return (cx + R * cos(radians(a)), cy + R * sin(radians(a)))
def circ(ax, cx, cy, R, ext=4):
    disc(ax, cx, cy, R, 'fixe', fill=False)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.2): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(70)
R = 14; cy = 44
cx1, cx2 = 24, 66
for cx in (cx1, cx2): circ(ax, cx, cy, R, ext=3)
arc(ax, cx1, cy, R + 3.5, 5, 365, 'varie', 0.9)
arc(ax, cx1, cy, 7, 5, 175, 'varie', 1.1)
dot(ax, P(cx1, cy, R, 180), 'resultat', 1.6)
arc(ax, cx2, cy, 7, -5, -85, 'varie', 1.1)
dot(ax, P(cx2, cy, R, 270), 'resultat', 1.6)
text(ax, cx1, 67, '540°', 'sujet', 'l', weight='bold')
text(ax, cx2, 67, '−90°', 'sujet', 'l', weight='bold')
text(ax, cx1, 21, '1 tour + ½ tour', 'varie', 's')
text(ax, cx2, 21, '¼ tour, sens horaire', 'varie', 's')
text(ax, cx1, 14, r'$P = (-1, 0)$', 'resultat', 's')
text(ax, cx2, 14, r'$P = (0, -1)$', 'resultat', 's')
text(ax, cx1, 7, r'$\sin = 0$ ; $\cos = -1$', 'resultat', 's')
text(ax, cx2, 7, r'$\sin = -1$ ; $\cos = 0$', 'resultat', 's')
save(fig, '28-073')
