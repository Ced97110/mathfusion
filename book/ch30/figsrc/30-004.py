import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(50)
x0, oy, A = 8, 28, 9
per = 17
n = 4
line(ax, [(x0, oy), (x0 + n * per + 10, oy)], 'fixe', dash=True)
text(ax, x0 + 1, oy - 12.5, 'position de repos', 'fixe', 's', ha='left')
gr(ax, lambda t: math.sin(2 * math.pi * t), x0, oy, per, A, 0, n, 'sujet')
text(ax, x0 + n * per + 4, oy, '…', 'sujet', 'l')
brace(ax, x0 + per, x0 + 2 * per, oy + A + 2.5, 'varie', '1 va-et-vient : 0,0023 s', False, depth=1.6)
brace(ax, x0, x0 + n * per + 8, 5, 'resultat', '440 va-et-vient par seconde', True)
save(fig, '30-004')
