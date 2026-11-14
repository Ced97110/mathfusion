import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
def _arc(cx, y, r, e, lower=True, n=24):
    s = -1 if lower else 1
    return [(cx + r * math.cos(math.pi * (1 - i / n)), y + s * e * math.sin(math.pi * (1 - i / n))) for i in range(n + 1)]
def cyl(ax, cx, y0, r, e, h, role='sujet', layers=1):
    poly(ax, [(cx - r, y0 + h)] + _arc(cx, y0, r, e) + [(cx + r, y0 + h)], role)
    for k in range(1, layers):
        line(ax, _arc(cx, y0 + h * k / layers, r, e), role, lw=0.45)
    ax.add_patch(Ellipse((cx, y0 + h), 2 * r, 2 * e, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2.5))
def cone(ax, cx, y0, r, e, h, role='sujet'):
    poly(ax, [(cx - r, y0)] + _arc(cx, y0, r, e) + [(cx, y0 + h)], role)
    line(ax, _arc(cx, y0, r, e, lower=False), role, lw=0.5, dash=True)
def equator(ax, cx, cy, R, role='sujet'):
    ax.add_patch(Ellipse((cx, cy), 2 * R, 0.6 * R, ec=COL[role], fc='none', lw=0.5, ls='--', zorder=2.5))
fig, ax = canvas(60)
y0, r, e = 14, 4, 1.5
line(ax, [(44, 6), (44, 58)], 'fixe', dash=True, lw=0.6)
text(ax, 22, 56, 'même hauteur', 'resultat', 'm')
text(ax, 66, 56, 'hauteur double', 'limite', 'm')
text(ax, 22, 50, 'cône = le tiers', 'resultat', 's')
text(ax, 66, 50, 'cône = un sixième', 'limite', 's')
cone(ax, 9, y0, r, e, 10, 'sujet'); cyl(ax, 31, y0, r, e, 10, 'autre')
arrow(ax, (15, 22), (25, 22), 'varie'); text(ax, 20, 26, '×3', 'varie', 'm')
cone(ax, 53, y0, r, e, 10, 'sujet'); cyl(ax, 78, y0, r, e, 20, 'autre')
arrow(ax, (59, 22), (72, 22), 'varie'); text(ax, 65.5, 26, '×6', 'varie', 'm')
text(ax, 9, 8, 'cône\nh = 5', 'sujet', 's'); text(ax, 31, 8, 'cylindre\nh = 5', 'autre', 's')
text(ax, 53, 8, 'cône\nh = 5', 'sujet', 's'); text(ax, 78, 8, 'cylindre\nh = 10', 'autre', 's')
save(fig, '11-134')
