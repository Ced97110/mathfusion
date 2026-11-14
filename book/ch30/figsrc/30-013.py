import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(56)
gx, oy, sx, A = 6, 28, 6.0, 12
line(ax, [(gx - 1, oy), (gx + 4 * math.pi * sx + 2, oy)], 'fixe', lw=0.7)
gr(ax, math.sin, gx, oy, sx, A, 0, 2 * math.pi, 'sujet', lw=1.4)
gr(ax, math.sin, gx, oy, sx, A, 2 * math.pi, 4 * math.pi, 'fixe', lw=1.4)
y1 = oy + A * math.sin(1)
line(ax, [(gx + 1 * sx, y1), (gx + (1 + 2 * math.pi) * sx, y1)], 'varie', lw=0.8, dash=True)
dot(ax, gx + sx, y1, 'varie'); dot(ax, gx + (1 + 2 * math.pi) * sx, y1, 'varie')
text(ax, gx + sx, oy - 4, '1', 'varie', 's'); text(ax, gx + (1 + 2 * math.pi) * sx, oy - 4, '7,2832', 'varie', 's')
text(ax, gx + (1 + math.pi) * sx, y1 + 3, 'même hauteur 0,8415', 'varie', 's')
brace(ax, gx, gx + 2 * math.pi * sx, 14, 'sujet', '2π : un tour', True)
brace(ax, gx + 2 * math.pi * sx, gx + 4 * math.pi * sx, 14, 'fixe', 'copie', True)
text(ax, 44, 51, 'on dessine un tour, puis on le recopie', 'encre', 's')
save(fig, '30-013')
