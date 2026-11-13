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
R, cy = 9, 30
for cx, k, n in ((15, 0.5, 2), (44, 1.0, 1), (73, 2.0, 0)):
    frame(ax, cx, cy, R, vert=False)
    y = cy + k * R
    line(ax, [(cx - R - 2, y), (cx + R + 2, y)], 'sujet', lw=1.0)
    if n == 2:
        x = math.sqrt(1 - k * k) * R
        dot(ax, cx + x, y, 'resultat', 1.4); dot(ax, cx - x, y, 'resultat', 1.4)
    if n == 1: dot(ax, cx, y, 'resultat', 1.4)
    text(ax, cx, 55, f'$k$ = {k:g}'.replace('.', ','), 'sujet', 'm')
    text(ax, cx, cy - R - 6, {2: '2 points', 1: '1 point', 0: 'aucun point'}[n], 'resultat' if n else 'limite', 's')
save(fig, '32-040')
