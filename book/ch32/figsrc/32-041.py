import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, tip=False, dash=False):
    n = max(2, int(abs(a1 - a0) / 3) + 1)
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / (n - 1)) for i in range(n)], role, lw, dash)
    if tip:
        s = 1 if a1 > a0 else -1
        arrow(ax, P(cx, cy, R, a1 - s * 6), P(cx, cy, R, a1), role, lw)
def dot(ax, x, y, role, r=1.2): disc(ax, x, y, r, role)
def frame(ax, cx, cy, R, vert=True):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
    if vert: line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)

fig, ax = canvas(76)
cx, cy, R = 34, 38, 20
frame(ax, cx, cy, R)
a, b = P(cx, cy, R, 30), P(cx, cy, R, 210)
line(ax, [a, b], 'fixe', dash=True)
arc(ax, cx, cy, R + 3.5, 30, 390, 'varie', lw=1.1, tip=True)
arc(ax, cx, cy, 11, 30, 210, 'autre', lw=1.1, tip=True)
dot(ax, *a, 'resultat', 1.6); dot(ax, *b, 'autre', 1.6)
text(ax, 71, 52, '30° et 390°', 'resultat', 's')
text(ax, 8, 16, '210°', 'autre', 's')
text(ax, cx, cy + R + 10, '+ 360° : un tour', 'varie', 's')
text(ax, cx, cy + 5, '+ ½ tour', 'autre', 's')
save(fig, '32-041')
