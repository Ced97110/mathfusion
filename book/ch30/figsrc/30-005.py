import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(74)
rows = [('hauteur de la cabine', 'sujet'), ("niveau d'eau du port", 'sujet'), ('écart du milieu de la corde', 'sujet')]
x0, w = 8, 70
for i, (lab, r) in enumerate(rows):
    oy = 62 - i * 14
    text(ax, x0, oy + 6.5, lab, r, 's', ha='left')
    gr(ax, lambda t: math.sin(2 * math.pi * t), x0, oy, w / 3, 4, 0, 3, r)
    line(ax, [(x0, oy), (x0 + w, oy)], 'fixe', lw=0.5)
oy = 14
text(ax, x0, oy + 11, 'nombre de pas depuis ce matin', 'varie', 's', ha='left')
line(ax, [(x0, oy - 3), (x0 + w, oy - 3)], 'fixe', lw=0.5)
pts = [(x0 + i * w / 12, oy - 3 + i * 1.0) for i in range(13)]
line(ax, pts, 'varie')
text(ax, 82, 68.5, 'se répète', 'sujet', 's', ha='right')
text(ax, 82, 25, 'ne se répète pas', 'varie', 's', ha='right')
save(fig, '30-005')
