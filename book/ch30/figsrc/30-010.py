import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(48); ax.set_ylim(12, 60)
cy, A = 36, 10
# panel 1 : unit circle
c1 = 15
ax.add_patch(Circle((c1, cy), A, ec=COL['fixe'], fc='none', lw=0.8, zorder=2))
line(ax, [(c1 - A - 2, cy), (c1 + A + 2, cy)], 'fixe', lw=0.6); line(ax, [(c1, cy - A - 2), (c1, cy + A + 2)], 'fixe', lw=0.6)
dot(ax, c1, cy + A, 'fixe')
text(ax, c1, 55, 'cercle unité', 'fixe', 's'); text(ax, c1, 22, '(cos θ ; sin θ)', 'fixe', 's')
# panels 2, 3
for gx, fn, role, ttl, lab, yv in ((32, math.sin, 'sujet', 'sinus', '(x ; sin x)', 1), (60, math.cos, 'autre', 'cosinus', '(x ; cos x)', 0)):
    sx = 3.4
    line(ax, [(gx, cy), (gx + 2 * math.pi * sx + 1, cy)], 'fixe', lw=0.6); line(ax, [(gx, cy - A - 2), (gx, cy + A + 2)], 'fixe', lw=0.6)
    gr(ax, fn, gx, cy, sx, A, 0, 2 * math.pi, role)
    px = gx + math.pi / 2 * sx
    line(ax, [(px, cy - 5), (px, cy + A * yv)], 'fixe', lw=0.5, dash=True)
    dot(ax, px, cy + A * yv, role, 1.4)
    text(ax, px, cy - 7.5, 'π/2', 'fixe', 's')
    text(ax, gx + 10.7, 55, ttl, role, 's'); text(ax, gx + 10.7, 22, lab, role, 's')
text(ax, 44, 14, 'même largeur x, hauteur différente', 'encre', 's', ha='center')
arrow(ax, (c1 + 2.5, cy + A), (32 + math.pi / 2 * 3.4 - 2.2, cy + A), 'varie', lw=1.0)
text(ax, 26, 50.5, 'lu sur le cercle', 'varie', 's')
save(fig, '30-010')
