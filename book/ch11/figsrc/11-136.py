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
fig, ax = canvas(72)
cx, cy, R = 44, 38, 24
disc(ax, cx, cy, R, 'sujet'); equator(ax, cx, cy, R)
for ang, lx, ly in ((90, 47, 50), (0, 56, 40.5), (225, 33.5, 32.5)):
    ex, ey = cx + R * math.cos(math.radians(ang)), cy + R * math.sin(math.radians(ang))
    arrow(ax, (cx, cy), (ex, ey), 'varie')
    disc(ax, ex, ey, 1.0, 'varie')
    text(ax, lx, ly, r'$r$', 'varie', 'm')
disc(ax, cx, cy, 1.0, 'encre')
text(ax, cx + 2, cy - 3.5, 'centre', 'encre', 's', ha='left')
text(ax, 44, 68, 'sphère de rayon $r$', 'sujet', 'l')
text(ax, 44, 8, 'tous les points : même distance $r$', 'varie', 's')
save(fig, '11-136')
