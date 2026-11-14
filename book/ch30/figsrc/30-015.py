import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(58)
gx, oy, sx, A = 8, 28, 10.0, 16
line(ax, [(gx, oy), (gx + 2 * math.pi * sx + 3, oy)], 'fixe', lw=0.7)
line(ax, [(gx, oy - A - 3), (gx, oy + A + 6)], 'fixe', lw=0.7)
gr(ax, math.sin, gx, oy, sx, A, 0, 2 * math.pi, 'sujet', lw=1.5)
gr(ax, math.cos, gx, oy, sx, A, 0, 2 * math.pi, 'autre', lw=1.5)
dot(ax, gx, oy + A, 'autre', 1.3); dot(ax, gx + math.pi / 2 * sx, oy + A, 'sujet', 1.3)
arrow(ax, (gx + 1.8, oy + A + 3.5), (gx + math.pi / 2 * sx - 1.8, oy + A + 3.5), 'resultat', lw=1.4)
text(ax, gx + math.pi / 4 * sx + 8, oy + A + 7, 'cosinus glissé de π/2', 'resultat', 's')
text(ax, gx - 3.5, oy + A, '1', 'fixe', 's')
text(ax, gx + math.pi * sx, oy + 3.2, 'π', 'fixe', 's'); text(ax, gx + 2 * math.pi * sx, oy + 3.2, '2π', 'fixe', 's')
text(ax, gx + 4.5 * sx, oy + A + 1, 'sinus', 'sujet', 's', ha='left'); text(ax, gx + 4.5 * sx, oy + A - 4, 'cosinus', 'autre', 's', ha='left')
line(ax, [(gx + math.pi / 2 * sx, oy + A), (gx + math.pi / 2 * sx, oy - 7.5)], 'fixe', lw=0.5, dash=True)
text(ax, gx + math.pi / 2 * sx, oy - 9.5, 'π/2', 'fixe', 's')
text(ax, gx, oy - 9.5, '0', 'fixe', 's')
save(fig, '30-015')
