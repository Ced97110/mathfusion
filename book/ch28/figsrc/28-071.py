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
poly(ax, [(cx, cy), (cx, cy + R + 4), (cx + R + 4, cy + R + 4), (cx + R + 4, cy)], 'resultat')
poly(ax, [(cx, cy), (cx, cy + R + 4), (cx - R - 4, cy + R + 4), (cx - R - 4, cy)], 'autre')
circ(ax, cx, cy, R, ext=4)
line(ax, [(cx, cy - R - 4), (cx, cy + R + 4)], 'sujet', lw=1.6)
p = P(cx, cy, R, 90)
dot(ax, p, 'sujet', 1.7)
text(ax, cx + 3, p[1] + 2, r'$P$', 'sujet', 'm', ha='left')
text(ax, cx + 16, cy + 12, 'quadrant I', 'resultat', 's')
text(ax, cx - 16, cy + 12, 'quadrant II', 'autre', 's')
text(ax, cx + 2, cy - 5, r'$x = 0$', 'sujet', 's', ha='left')
text(ax, cx + 2, 4, 'sur la frontière : aucun quadrant', 'sujet', 's', ha='center') if False else None
text(ax, 44, 4, 'ni à droite, ni à gauche', 'sujet', 's')
save(fig, '28-071')
