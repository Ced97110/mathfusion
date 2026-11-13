import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(62)
cx, cy, R = 22, 30, 14
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=2))
line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', lw=0.6)
line(ax, [(cx, cy), (cx - R, cy)], 'sujet', lw=2.2)
dot(ax, cx - R, cy, 'sujet', 1.4); dot(ax, cx, cy, 'fixe', 0.8)
text(ax, cx, cy - 4, 'O', 'fixe', 's'); text(ax, cx - R - 1.5, cy + 4, 'P', 'sujet', 's')
text(ax, cx, cy + R + 4, 'OH vers la gauche', 'sujet', 's')
text(ax, cx, cy - R - 4, 'demi-tour', 'fixe', 's')
gx, sx = 52, 5.0
line(ax, [(gx, cy), (gx + 2 * math.pi * sx + 2, cy)], 'fixe', lw=0.6)
line(ax, [(gx, cy - R - 2), (gx, cy + R + 2)], 'fixe', lw=0.6)
gr(ax, math.cos, gx, cy, sx, R, 0, 2 * math.pi, 'sujet')
X = gx + math.pi * sx
dot(ax, X, cy - R, 'resultat', 1.4)
dot(ax, X, cy + R, 'limite', 1.4, fill=False)
line(ax, [(X, cy), (X, cy + R)], 'limite', dash=True, lw=0.7)
text(ax, X, cy - R - 4, '(π ; −1) juste', 'resultat', 's')
text(ax, X, cy + R + 4, '(π ; 1) faux', 'limite', 's')
save(fig, '30-016')
