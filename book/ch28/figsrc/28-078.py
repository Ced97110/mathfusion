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
fig, ax = canvas(78)
cx, cy, R = 30, 42, 24
circ(ax, cx, cy, R, ext=3)
p = P(cx, cy, R, 40)
arc(ax, cx, cy, R + 3.5, 3, 398, 'varie', 0.9)
line(ax, [(cx, cy), p], 'sujet', lw=1.2)
line(ax, [p, (cx + R + 7, p[1])], 'resultat', lw=0.8, dash=True)
line(ax, [(cx + R + 7, cy), (cx + R + 7, p[1])], 'resultat', lw=2.0)
dot(ax, p, 'sujet', 1.5)
text(ax, cx + R + 9, (cy + p[1]) / 2, '10,93 cm', 'resultat', 's', ha='left')
text(ax, cx + 5, cy - 8, '17 cm', 'sujet', 's', ha='left') if False else None
text(ax, cx + 6, cy + 3, '40°', 'sujet', 's', ha='left')
text(ax, 72, 70, '400° = 360° + 40°', 'varie', 's')
text(ax, 44, 7, r'$17 \times \sin 40° \approx 17 \times 0{,}6428$', 'sujet', 's')
text(ax, 44, 1.8, 'même hauteur qu’à 40°', 'resultat', 's') if False else None
text(ax, 72, 62, 'manivelle : 17 cm', 'sujet', 's')
save(fig, '28-078')
