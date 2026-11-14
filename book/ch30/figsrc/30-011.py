import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(56)
gx, oy, sx, A = 8, 30, 11.0, 12
line(ax, [(gx - 2, oy), (gx + 2 * math.pi * sx + 3, oy)], 'fixe', lw=0.7)
gr(ax, math.sin, gx, oy, sx, A, 0, 2 * math.pi, 'sujet', lw=1.2)
pts = [(0, 0, 'sujet', '(0 ; 0)', (0, -5, 'left')), (math.pi / 2, 1, 'resultat', '(π/2 ; 1)', (0, 4.5, 'center')),
       (math.pi, 0, 'sujet', '(π ; 0)', (1, 4.5, 'left')), (3 * math.pi / 2, -1, 'varie', '(3π/2 ; −1)', (0, -4.5, 'center')),
       (2 * math.pi, 0, 'sujet', '(2π ; 0)', (-1, 4.5, 'right'))]
for t, v, role, lab, (dx, dy, ha) in pts:
    X, Y = gx + t * sx, oy + v * A
    line(ax, [(X, oy), (X, Y)], 'fixe', lw=0.4, dash=True) if v else None
    dot(ax, X, Y, role)
    text(ax, X + dx, Y + dy, lab, role, 's', ha=ha)
for i in range(1, 5):
    brace(ax, gx + (i - 1) * math.pi / 2 * sx + 0.5, gx + i * math.pi / 2 * sx - 0.5, 9, 'fixe', None, True, depth=1.4)
text(ax, 44, 3.5, '4 quarts de tour', 'fixe', 's')
save(fig, '30-011')
