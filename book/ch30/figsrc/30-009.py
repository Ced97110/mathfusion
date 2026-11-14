import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(66)
cx, cy, R = 22, 28, 16
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=2))
line(ax, [(cx - R - 2, cy), (cx + R + 3, cy)], 'fixe', lw=0.6)
arc = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in [math.pi / 2 * i / 40 for i in range(41)]]
line(ax, arc, 'varie', lw=2.0)
dot(ax, cx + R, cy, 'fixe'); dot(ax, cx, cy + R, 'sujet')
line(ax, [(cx, cy), (cx, cy + R)], 'sujet', lw=1.6)
text(ax, cx + R + 3, cy - 3, 'A', 'fixe', 's'); text(ax, cx + 3, cy + R + 3, 'P', 'sujet', 's')
text(ax, cx - 4, cy + R / 2, 'HP', 'sujet', 's'); text(ax, cx + 7.5, cy + 7.5, 'θ', 'varie', 'm')
gx, sx = 52, 5.0
th = math.pi / 2
line(ax, [(gx, cy), (gx + 2 * math.pi * sx + 2, cy)], 'fixe', lw=0.8)
line(ax, [(gx, cy - R - 2), (gx, cy + R + 2)], 'fixe', lw=0.8)
gr(ax, math.sin, gx, cy, sx, R, 0, 2 * math.pi, 'fixe', lw=0.6, dash=True)
M = (gx + th * sx, cy + R)
arrow(ax, (gx, cy - 3.5), (M[0], cy - 3.5), 'varie')
text(ax, gx + th * sx / 2, cy - 7, '1. reporter θ', 'varie', 's')
arrow(ax, (M[0] + 3, cy), (M[0] + 3, M[1]), 'sujet')
text(ax, 69, cy + 9, '2. monter\nde HP', 'sujet', 's', ha='left')
dot(ax, *M, 'resultat', 1.4)
text(ax, M[0] - 1, M[1] + 4.5, '3. M (θ ; sin θ)', 'resultat', 's')
text(ax, 22, 58, 'sur le cercle', 'fixe', 's')
save(fig, '30-009')
