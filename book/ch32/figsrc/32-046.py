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
cx, cy, R, gx = 28, 36, 26, 70
frame(ax, cx, cy, R, vert=False)
line(ax, [(gx, cy - R), (gx, cy + R)], 'fixe', lw=1.0)
for v in (-1, 0, 1): line(ax, [(gx - 1.2, cy + v * R), (gx + 1.2, cy + v * R)], 'fixe', lw=0.8)
text(ax, gx, cy + R + 3.5, '1', 'fixe', 's'); text(ax, gx, cy - R - 3.5, '−1', 'fixe', 's')
for k in (0.9, 0.5, -0.2):
    y = cy + k * R
    x = cx + R * math.sqrt(1 - k * k)
    line(ax, [(x, y), (gx, y)], 'varie', dash=True)
    dot(ax, x, y, 'sujet', 1.4); dot(ax, gx, y, 'varie', 1.5)
    text(ax, gx + 3, y, f'{k:g}'.replace('.', ',').replace('-', '−'), 'varie', 's', ha='left')
text(ax, 38, 70, '$k$ : hauteur visée', 'varie', 'm')
save(fig, '32-046')
