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
cx, cy, R = 30, 36, 24
frame(ax, cx, cy, R)
p = P(cx, cy, R, 40)
line(ax, [(cx, cy), p], 'sujet', lw=1.3)
line(ax, [p, (p[0], cy)], 'resultat', dash=True, lw=1.1)
arc(ax, cx, cy, 9, 0, 40, 'varie', lw=1.2)
dot(ax, *p, 'sujet', 1.6)
text(ax, cx + 13.5, cy + 3.2, '$\\theta$', 'varie', 'm')
text(ax, p[0] + 3, p[1] + 3, '$P$', 'sujet', 'm')
text(ax, p[0] + 3, (p[1] + cy) / 2, '$\\sin\\,\\theta = k$', 'resultat', 's', ha='left')
text(ax, 44, 7, '$\\theta$ : angle cherché', 'varie', 'm')
save(fig, '32-045')
