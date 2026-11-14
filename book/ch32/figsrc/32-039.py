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
cx, cy, R = 44, 34, 24
frame(ax, cx, cy, R)
a, b = P(cx, cy, R, 30), P(cx, cy, R, 150)
line(ax, [b, a], 'resultat', dash=True)
arc(ax, cx, cy, 9, 0, 30, 'sujet'); arc(ax, cx, cy, 9, 180, 150, 'varie')
line(ax, [(cx, cy), a], 'sujet', lw=1.1); line(ax, [(cx, cy), b], 'varie', lw=1.1)
dot(ax, *a, 'sujet', 1.5); dot(ax, *b, 'varie', 1.5)
text(ax, cx + 14, cy + 2, '30°', 'sujet', 's'); text(ax, cx - 14, cy + 2, '30°', 'varie', 's')
text(ax, a[0] + 11, a[1] + 4, '$\\alpha$ = 30°', 'sujet', 's')
text(ax, 12, b[1] + 6, '180° − $\\alpha$\n= 150°', 'varie', 's')
text(ax, 34, cy + 20, 'même\nhauteur', 'resultat', 's')
save(fig, '32-039')
