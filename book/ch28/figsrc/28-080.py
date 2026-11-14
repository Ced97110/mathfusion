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
fig, ax = canvas(72)
cx, cy, R = 44, 36, 24
circ(ax, cx, cy, R, ext=3)
a = 50
Pp, Q, Rr, S = P(cx, cy, R, a), P(cx, cy, R, 180 - a), P(cx, cy, R, 180 + a), P(cx, cy, R, -a)
poly(ax, [Pp, Q, Rr, S], 'fixe')
circ(ax, cx, cy, R, ext=3)
for pt, role, s, dx, dy, ha in [(Pp, 'sujet', r'$P\ (x, y)$', 2.5, 3, 'left'), (Q, 'varie', r'$Q\ (-x, y)$', -2.5, 3, 'right'),
                                (Rr, 'autre', r'$R\ (-x, -y)$', -2.5, -3, 'right'), (S, 'varie', r'$S\ (x, -y)$', 2.5, -3, 'left')]:
    dot(ax, pt, role, 1.6); text(ax, pt[0] + dx, pt[1] + dy, s, role, 's', ha=ha)
text(ax, 44, 68, 'mêmes nombres, signes changés', 'sujet', 's')
save(fig, '28-080')
