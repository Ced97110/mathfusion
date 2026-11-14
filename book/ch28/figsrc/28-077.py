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
fig, ax = canvas(64)
rows = [(48, '460°', '− 1 tour', '100°', 'quadrant II'), (27, '−460°', '+ 2 tours', '260°', 'quadrant III'),
        (6, '840°', '− 2 tours', '120°', r'$\cos 840° = \cos 120°$')]
for y, a, k, b, c in rows:
    box(ax, 2, y, 16, 10, 'sujet', label=a, size='m')
    arrow(ax, (19.5, y + 5), (38.5, y + 5), 'varie')
    text(ax, 29, y + 9.2, k, 'varie', 's')
    box(ax, 40, y, 16, 10, 'resultat', label=b, size='m')
    text(ax, 58.5, y + 5, c, 'resultat', 's', ha='left')
save(fig, '28-077')
