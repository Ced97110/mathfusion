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
cx, cy, R = 44, 36, 18
circ(ax, cx, cy, R, ext=3)
for a, s, ha, dx, dy in [(0, '0° et 360°\n(1, 0)', 'left', 3, 0), (90, '90° : (0, 1)', 'center', 0, 4.5),
                         (180, '180°\n(−1, 0)', 'right', -3, 0), (270, '270° : (0, −1)', 'center', 0, -4.5)]:
    p = P(cx, cy, R, a); dot(ax, p, 'resultat', 1.6)
    text(ax, p[0] + dx, p[1] + dy, s, 'resultat', 's', ha=ha, va='center')
arc(ax, cx, cy, 8, 5, 85, 'varie', 1.1)
text(ax, cx + 7, cy + 9.5, '¼ tour', 'varie', 's')
text(ax, 44, 5, 'chaque point est à la distance 1', 'sujet', 's')
save(fig, '28-072')
