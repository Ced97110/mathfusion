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
cx, cy, R = 24, 33, 20
circ(ax, cx, cy, R, ext=3)
p = P(cx, cy, R, 60)
line(ax, [(cx, cy), p], 'sujet', lw=1.1)
line(ax, [p, (p[0], cy)], 'resultat', lw=0.9, dash=True)
line(ax, [(cx, cy), (p[0], cy)], 'resultat', lw=2.0)
dot(ax, p, 'sujet', 1.5)
text(ax, p[0], cy - 3.5, r'$\cos = 0{,}5$', 'resultat', 's')
labs = [(52, 'k = 0', '60°'), (40, 'k = 1', '420°'), (28, 'k = −1', '−300°')]
for y, k, a in labs:
    box(ax, 52, y, 34, 9, 'varie', label=f'{a}   ({k})', size='s')
    arrow(ax, (52, y + 4.5), (p[0] + 1.5, p[1] - 0.3 if y == 52 else p[1] - 1.5), 'varie', lw=0.7)
text(ax, 44, 8, 'même point : même cosinus', 'resultat', 's') if False else None
text(ax, 70, 12, 'même point P', 'sujet', 's')
text(ax, 70, 6, 'même cosinus', 'resultat', 's')
save(fig, '28-075')
