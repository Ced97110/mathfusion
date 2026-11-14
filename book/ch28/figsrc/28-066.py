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
rows = [(44, 34, 'I', '+', '+', '+', 'resultat'), (4, 34, 'II', '−', '+', '−', 'fixe'),
        (4, 6, 'III', '−', '−', '+', 'resultat'), (44, 6, 'IV', '+', '−', '−', 'fixe')]
for x, y, n, c, s, t, role in rows:
    box(ax, x, y, 40, 28, role, r=0.6)
    text(ax, x + 4, y + 24, n, 'sujet', 'l', ha='left', weight='bold')
    text(ax, x + 20, y + 11, f'cos {c}   sin {s}   tan {t}', 'encre', 's')
text(ax, 44, 64, 'vert : tan positive', 'resultat', 's')
save(fig, '28-066')
