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
fig, ax = canvas(66)
cx, cy, R = 44, 30, 24
circ(ax, cx, cy, R, ext=4)
line(ax, [(cx, cy - R - 4), (cx, cy + R + 4)], 'varie', lw=1.4)
p1, p2 = P(cx, cy, R, 60), P(cx, cy, R, 120)
line(ax, [(cx, cy), p1], 'sujet', lw=1.0); line(ax, [(cx, cy), p2], 'autre', lw=1.0)
line(ax, [p2, p1], 'resultat', lw=1.0, dash=True)
dot(ax, p1, 'sujet', 1.5); dot(ax, p2, 'autre', 1.5)
text(ax, p1[0] + 2.5, p1[1] + 2.5, '60°', 'sujet', 's', ha='left')
text(ax, p2[0] - 2.5, p2[1] + 2.5, '120°', 'autre', 's', ha='right')
text(ax, cx + 2, cy + R + 6, 'axe de symétrie', 'varie', 's', ha='left')
text(ax, cx, p1[1] - 3.5, 'même hauteur', 'resultat', 's')
text(ax, 44, 4, r'$\sin 60° = \sin 120° \approx 0{,}866$', 'resultat', 's')
save(fig, '28-079')
