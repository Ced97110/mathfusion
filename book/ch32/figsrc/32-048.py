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

fig, ax = canvas(66)
text(ax, 44, 59, '360°$n$ : $n$ tours', 'encre', 'm')
R, cy = 10, 34
for cx, n, lab, deg in ((15, 2, '$n$ = 2', '720°'), (44, -1, '$n$ = −1', '−360°'), (73, 0, '$n$ = 0', '0°')):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.7)
    if n == 2:
        arc(ax, cx, cy, R, 0, 340, 'varie', tip=True); arc(ax, cx, cy, 6, 0, 340, 'varie', tip=True)
    if n == -1: arc(ax, cx, cy, R, 0, -340, 'varie', tip=True)
    dot(ax, cx + R, cy, 'sujet', 1.4)
    text(ax, cx, cy + R + 6, lab, 'sujet', 'm')
    text(ax, cx, cy - R - 6, deg, 'resultat', 'm')
save(fig, '32-048')
