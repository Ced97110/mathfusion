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
fig, ax = canvas(76)
cx, cy, R = 38, 40, 24
circ(ax, cx, cy, R, ext=3)
p = P(cx, cy, R, 210)
line(ax, [(cx, cy), p], 'sujet', lw=1.1)
dot(ax, p, 'sujet', 1.5)
line(ax, [p, (p[0], cy)], 'fixe', lw=0.8, dash=True)
arrow(ax, (p[0], cy - 0.3), (p[0], p[1] + 0.3), 'resultat', lw=1.4)
text(ax, p[0] - 1.5, (p[1] + cy) / 2, '8,5 cm', 'resultat', 's', ha='right')
text(ax, cx + 7, cy - 8, '17 cm', 'sujet', 's', rot=0)
arc(ax, cx, cy, 6, 0, 205, 'varie', 0.8)
text(ax, cx + 9, cy + 5, '210°', 'varie', 's')
text(ax, 74, 56, 'distance : 8,5', 'sujet', 's')
text(ax, 74, 48, 'signe − : en dessous', 'varie', 's', ha='center')
text(ax, 44, 6, 'hauteur = −8,5 cm', 'resultat', 'm', weight='bold')
save(fig, '28-069')
