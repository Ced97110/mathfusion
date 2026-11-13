import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(52)
gx, oy, sx, A = 44, 28, 6.0, 12
line(ax, [(gx - 2 * math.pi * sx - 2, oy), (gx + 2 * math.pi * sx + 3, oy)], 'fixe', lw=0.7)
line(ax, [(gx, oy - A - 3), (gx, oy + A + 3)], 'fixe', lw=0.7)
gr(ax, math.sin, gx, oy, sx, A, 0, 2 * math.pi, 'fixe', lw=1.4)
gr(ax, math.sin, gx, oy, sx, A, -2 * math.pi, 0, 'sujet', lw=1.4)
X, Y = gx - math.pi / 2 * sx, oy - A
dot(ax, X, Y, 'varie', 1.4)
text(ax, X + 3, Y - 3.5, '(−π/2 ; −1)', 'varie', 's', ha='left')
for t, s in ((-2 * math.pi, '−2π'), (-math.pi, '−π'), (math.pi, 'π'), (2 * math.pi, '2π')):
    line(ax, [(gx + t * sx, oy), (gx + t * sx, oy - A - 3)], 'fixe', lw=0.4, dash=True)
    text(ax, gx + t * sx, oy - A - 6, s, 'fixe', 's')
text(ax, gx - math.pi * sx, 46, 'angles négatifs', 'sujet', 's'); text(ax, gx + math.pi * sx, 46, 'angles positifs', 'fixe', 's')
save(fig, '30-014')
