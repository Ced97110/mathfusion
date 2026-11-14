import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(70)
def ghost(x, w, h, y=8):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL['limite'], fc='none', lw=0.9, ls='--', zorder=4))
text(ax, 20, 64, 'taxi : droite', 'sujet', 's')
for i, v in enumerate((3, 5, 7)):
    bx = 6 + i * 11
    h = v * 4.5
    box(ax, bx, 8, 8, h, 'sujet', label=str(v), size='s', r=0.5)
    text(ax, bx + 4, 4.5, str(i), 'fixe', 's')
ghost(28, 8, 3 * 4.5)
arrow(ax, (20, 53), (30, 24.5), 'limite', lw=0.9)
text(ax, 20, 56.5, 'ne revient pas à 3', 'limite', 's')
text(ax, 20, 1.8, 'km', 'fixe', 's')
text(ax, 62, 64, 'carré : parabole', 'autre', 's')
vs = [4, 1, 0, 1, 4, 9, 16, 25]
for i, v in enumerate(vs):
    bx = 46 + i * 5
    role = 'autre' if i < 5 else 'varie'
    h = max(v * 1.9, 0.4)
    ax.add_patch(Rectangle((bx, 8), 4, h, ec=COL[role], fc=FILL[role], lw=0.7, zorder=2))
    text(ax, bx + 2, 8 + h + 2.2, str(v), role, 's')
    text(ax, bx + 2, 4.5, f'{i - 2}'.replace('-', '−'), 'fixe', 's')
for i, v in enumerate((4, 1, 0)):
    ghost(46 + (5 + i) * 5, 4, max(v * 1.9, 0.4))
arrow(ax, (58, 42), (71.5, 14), 'limite', lw=0.9)
text(ax, 58, 45.5, 'ne revient pas à 4, 1, 0', 'limite', 's')
text(ax, 62, 1.8, 'nombre de départ', 'fixe', 's')
line(ax, [(37, 6), (37, 62)], 'fixe', dash=True, lw=0.5)
save(fig, '30-007')
