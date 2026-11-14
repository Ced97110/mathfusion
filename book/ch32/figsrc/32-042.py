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
text(ax, 44, 66, '$\\sin\\,\\theta$ = 0,5', 'encre', 'm')
for y, role, vals, cap in ((48, 'sujet', (-330, 30, 390), '$\\theta = \\alpha$ + 360°$n$'),
                           (22, 'autre', (-210, 150, 510), '$\\theta$ = 180° − $\\alpha$ + 360°$n$')):
    line(ax, [(X(-360), y), (X(540), y)], 'fixe', lw=0.6)
    text(ax, 2, y + 9, cap, role, 's', ha='left')
    for i, v in enumerate(vals):
        dot(ax, X(v), y, role, 1.5)
        text(ax, X(v), y - 4.5, f'{v}°'.replace('-', '−'), role, 's')
        if i < 2:
            arrow(ax, (X(v) + 2, y + 3), (X(vals[i + 1]) - 2, y + 3), 'varie', lw=0.9)
            text(ax, (X(v) + X(vals[i + 1])) / 2, y + 6, '+ 360°', 'varie', 's')
save(fig, '32-042')
