import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(66)
cx, cy, R = 22, 34, 16
th = 2 * math.pi / 3
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=2))
line(ax, [(cx - R - 2, cy), (cx + R + 3, cy)], 'fixe', lw=0.6)
gr(ax, lambda t: 0, 0, 0, 1, 1, 0, 1, 'fixe', n=1)
arc = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in [th * i / 60 for i in range(61)]]
line(ax, arc, 'varie', lw=2.0)
P = (cx + R * math.cos(th), cy + R * math.sin(th))
line(ax, [(cx, cy), P], 'fixe', lw=0.6)
dot(ax, cx + R, cy, 'fixe'); dot(ax, *P, 'sujet')
text(ax, cx + R + 3, cy - 3, 'A', 'fixe', 's'); text(ax, P[0] - 3, P[1] + 2.5, 'P', 'sujet', 's')
text(ax, cx + 6.5, cy + 8, 'θ', 'varie', 'm')
gx, sx = 52, 5.0
line(ax, [(gx, cy), (gx + 2 * math.pi * sx + 2, cy)], 'fixe', lw=0.8)
line(ax, [(gx, cy - R - 2), (gx, cy + R + 2)], 'fixe', lw=0.8)
gr(ax, math.sin, gx, cy, sx, R, 0, 2 * math.pi, 'sujet')
line(ax, [(gx, cy), (gx + th * sx, cy)], 'varie', lw=2.0)
M = (gx + th * sx, cy + R * math.sin(th))
line(ax, [P, M], 'resultat', dash=True)
dot(ax, *M, 'resultat')
text(ax, M[0] + 2.5, M[1] + 3, 'M', 'resultat', 's')
text(ax, gx + th * sx / 2, cy - 3, 'θ', 'varie', 's')
text(ax, gx + math.pi * sx, cy - R - 4, 'π', 'fixe', 's'); text(ax, gx + 2 * math.pi * sx, cy - R - 4, '2π', 'fixe', 's')
text(ax, 22, 58, 'cercle de rayon 1', 'fixe', 's'); text(ax, 68, 58, 'graphe du sinus', 'sujet', 's')
save(fig, '30-008')
