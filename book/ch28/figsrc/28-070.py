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
cx, cy, R = 44, 35, 22
circ(ax, cx, cy, R, ext=3)
for a, s, ha, dx, dy in [(0, '(1, 0)', 'left', 2.5, 3), (90, '(0, 1)', 'center', 0, 4), (180, '(−1, 0)', 'right', -2.5, 3), (270, '(0, −1)', 'center', 0, -4)]:
    p = P(cx, cy, R, a); dot(ax, p, 'sujet', 1.5)
    text(ax, p[0] + dx, p[1] + dy, s, 'sujet', 's', ha=ha)
p = P(cx, cy, R, 130)
line(ax, [(cx, cy), p], 'fixe', lw=0.8); dot(ax, p, 'fixe', 1.3)
text(ax, p[0] - 2, p[1] + 3, '130°', 'fixe', 's', ha='right')
text(ax, 20, 66, 'dans un quadrant', 'fixe', 's')
text(ax, 70, 66, 'sur un axe', 'sujet', 's', weight='bold')
text(ax, 44, 5, 'angle quadrantal : côté final sur un axe', 'sujet', 's') if False else None
text(ax, 44, 5, 'quadrantal : sur un axe', 'sujet', 'm')
save(fig, '28-070')
