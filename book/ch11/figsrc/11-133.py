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
y0, h, r, e = 12, 30, 11, 3.5
cyl(ax, 24, y0, r, e, h, 'autre')
cone(ax, 64, y0, r, e, h, 'sujet')
line(ax, [(36, y0 + h), (62, y0 + h)], 'fixe', dash=True)
line(ax, [(36, y0), (52, y0)], 'fixe', dash=True)
arrow(ax, (44, y0), (44, y0 + h), 'varie', both=True)
text(ax, 46.5, y0 + h / 2, r'$h$', 'varie', 'm', ha='left')
text(ax, 24, 5, 'cylindre', 'autre', 's')
text(ax, 64, 5, 'cône', 'sujet', 's')
text(ax, 44, 5, 'même base', 'fixe', 's')
text(ax, 24, 52, 'disque en haut', 'autre', 's')
text(ax, 80, 49, 'pointe', 'sujet', 's')
arrow(ax, (76, 47.8), (65.5, y0 + h + 0.8), 'sujet')
save(fig, '11-133')
