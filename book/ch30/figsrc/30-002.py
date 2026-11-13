import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(46)
x0, k, h = 6, 1.9, 9
vals = [5.86, 14.14, 14.14, 5.86]
text(ax, 44, 40, 'montée par minute (total 40 m)', 'encre', 's')
text(ax, 6, 33, 'une droite', 'fixe', 's', ha='left')
x = x0
for i in range(4):
    box(ax, x, 22.5, 10 * k, h, 'fixe', label='10', size='s'); x += 10 * k
text(ax, 6, 15.5, 'la cabine', 'sujet', 's', ha='left')
x = x0
for v in vals:
    box(ax, x, 4, v * k, h, 'sujet', label=f'{v:.2f}'.replace('.', ','), size='s'); x += v * k
text(ax, 82, 33, 'égaux', 'fixe', 's', ha='right')
text(ax, 82, 15.5, 'inégaux', 'sujet', 's', ha='right')
save(fig, '30-002')
