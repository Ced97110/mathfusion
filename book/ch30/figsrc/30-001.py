import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(62)
cx, cy, R = 24, 28, 20
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=2))
line(ax, [(2, 6), (46, 6)], 'fixe', lw=1.0)
text(ax, 10, 2.8, 'sol', 'fixe', 's')
line(ax, [(cx, cy), (cx + R * 0.8, cy + R * 0.6)], 'sujet')
text(ax, cx + 1, cy + 12.5, 'rayon 20 m', 'sujet', 's', ha='left')
dot(ax, cx, cy, 'fixe', 0.8)
text(ax, cx - 2, cy - 3, 'centre\n22 m', 'fixe', 's', ha='right')
dot(ax, cx, cy - R, 'varie'); dot(ax, cx, cy + R, 'resultat')
text(ax, cx + 2.5, 11.5, '2 m', 'varie', 's', ha='left')
text(ax, cx, 51, '42 m', 'resultat', 's')
x0, sx = 52, 3.4
line(ax, [(x0, 6), (x0 + 8 * sx + 2, 6)], 'fixe')
gr(ax, lambda t: 22 - 20 * math.cos(2 * math.pi * t / 8), x0, 6, sx, 1.0, 0, 8, 'sujet')
for t, role in ((0, 'varie'), (4, 'resultat'), (8, 'varie')):
    dot(ax, x0 + t * sx, 6 + 22 - 20 * math.cos(2 * math.pi * t / 8), role)
    text(ax, x0 + t * sx, 2.8, f'{t}', 'fixe', 's')
text(ax, x0 + 4 * sx, 57, 'hauteur selon le temps', 'sujet', 's')
text(ax, x0 + 8 * sx + 3, 2.8, 'min', 'fixe', 's', ha='left')
save(fig, '30-001')
