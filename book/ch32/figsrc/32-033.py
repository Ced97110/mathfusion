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

fig, ax = canvas(64)
cx, cy, R = 22, 30, 15
frame(ax, cx, cy, R)
Pp = P(cx, cy, R, 30)
line(ax, [(cx, cy), Pp], 'sujet', lw=1.2)
arc(ax, cx, cy, 5, 0, 30, 'varie')
line(ax, [Pp, (Pp[0], cy)], 'fixe', dash=True)
dot(ax, *Pp, 'sujet')
text(ax, cx + 9, cy + 2.4, '30°', 'varie', 's')
text(ax, cx, cy + R + 7, 'arcsin 0,5', 'sujet', 'm')
text(ax, cx, cy - R - 5, 'un angle', 'sujet', 's')
f = numberline(ax, 52, 80, cy, 0, 2, step=0.5, labels=False, arrow_right=False)
for v in (0, 1, 2): text(ax, f(v), cy - 4, f'{v}', 'autre', 's')
dot(ax, f(0.5), cy, 'fixe'); text(ax, f(0.5), cy + 4, '0,5', 'fixe', 's')
dot(ax, f(2), cy, 'autre')
text(ax, 66, cy + R + 7, '1 ÷ sin 30°', 'autre', 'm')
text(ax, 66, cy - R - 5, 'un nombre', 'autre', 's')
text(ax, 44.5, cy, '≠', 'limite', 'xl')
save(fig, '32-033')
