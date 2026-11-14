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

fig, ax = canvas(70)
cx, cy, R = 28, 34, 24
ax.add_patch(Wedge((cx, cy), R, -90, 90, fc=FILL['sujet'], ec='none', zorder=1))
frame(ax, cx, cy, R)
h = 0.5 * R
line(ax, [P(cx, cy, R, 150), P(cx, cy, R, 30)], 'fixe', dash=True)
a, b = P(cx, cy, R, 30), P(cx, cy, R, 150)
dot(ax, *a, 'resultat', 1.5); dot(ax, *b, 'limite', 1.5)
text(ax, 57, a[1], '30° : choisi', 'resultat', 's', ha='left')
text(ax, 2, 62, '150° : écarté', 'limite', 's', ha='left')
text(ax, cx + 9, cy - 11, 'moitié droite', 'sujet', 's')
text(ax, cx - 2, a[1] + 3.5, 'hauteur 0,5', 'fixe', 's')
save(fig, '32-034')
