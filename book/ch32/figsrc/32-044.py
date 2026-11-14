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

fig, ax = canvas(72)
X = lambda v: 8 + (v + 360) / 900 * 72
rows = ((58, 'solution : un angle précis'), (38, 'angle principal : la touche'), (18, 'solution générale : écriture'))
for y, cap in rows:
    line(ax, [(X(-360), y), (X(540), y)], 'fixe', lw=0.6)
    text(ax, 2, y + 7, cap, 'encre', 's', ha='left')
dot(ax, X(150), 58, 'autre', 1.6); text(ax, X(150), 53.5, '150°', 'autre', 's')
dot(ax, X(30), 38, 'sujet', 1.6); text(ax, X(30), 33.5, '30°', 'sujet', 's')
for v in (-330, 30, 390): dot(ax, X(v), 18, 'sujet', 1.6)
for v in (-210, 150, 510): dot(ax, X(v), 18, 'autre', 1.6)
text(ax, 22, 11, '30° + 360°$n$', 'sujet', 's'); text(ax, 44, 11, 'ou', 'encre', 's'); text(ax, 66, 11, '150° + 360°$n$', 'autre', 's')
save(fig, '32-044')
