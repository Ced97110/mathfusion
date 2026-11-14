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
cx, cy, R = 34, 36, 24
frame(ax, cx, cy, R)
arc(ax, cx, cy, R, -90, 90, 'sujet', lw=2.6)
line(ax, [P(cx, cy, R, 150), P(cx, cy, R, 30)], 'fixe', dash=True)
a, b = P(cx, cy, R, 30), P(cx, cy, R, 150)
dot(ax, *a, 'resultat', 1.5); dot(ax, *b, 'fixe', 1.5)
dot(ax, cx, cy + R, 'sujet'); dot(ax, cx, cy - R, 'sujet')
text(ax, cx, cy + R + 4, '90°', 'sujet', 's'); text(ax, cx, cy - R - 4, '−90°', 'sujet', 's')
text(ax, a[0] + 6, a[1] + 1, '30°', 'resultat', 's')
text(ax, b[0] - 6, b[1] + 1, '150°', 'fixe', 's')
text(ax, cx + 11, cy - 9, 'moitié droite', 'sujet', 's')
text(ax, cx, a[1] + 3.5, 'hauteur 0,5', 'fixe', 's')
save(fig, '32-035')
