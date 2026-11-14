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
rows = [('pavé', r'$L\times l\times h$', 'sujet'), ('cube', r'$c^3$', 'sujet'), ('cylindre', r'$\pi r^2 h$', 'sujet'),
        ('cône', r'$\frac{1}{3}\pi r^2 h$', 'autre'), ('sphère', r'$\frac{4}{3}\pi r^3$', 'fixe')]
for i, (nm, fm, role) in enumerate(rows):
    yc = 64 - 12 * i
    line(ax, [(2, yc + 6), (86, yc + 6)], 'fixe', lw=0.4)
    text(ax, 20, yc, nm, role, 'm', ha='left'); text(ax, 42, yc, fm, role, 'm', ha='left')
line(ax, [(2, 10), (86, 10)], 'fixe', lw=0.4)
cubes(ax, [(0, 0, 0), (1, 0, 0)], (7, 60), 3.0, 'sujet')
cubes(ax, [(0, 0, 0)], (9, 48), 4.0, 'sujet')
cyl(ax, 9, 36, 4.5, 1.6, 7, 'sujet')
cone(ax, 9, 24, 4.5, 1.6, 8, 'autre')
disc(ax, 9, 16, 4.5, 'fixe'); equator(ax, 9, 16, 4.5, 'fixe')
line(ax, [(63, 68), (63, 36)], 'sujet', lw=1.0)
text(ax, 66, 52, 'base\n× hauteur', 'sujet', 's', ha='left')
text(ax, 66, 28, 'un tiers\ndu cylindre', 'autre', 's', ha='left')
text(ax, 66, 16, 'ni base\nni hauteur', 'fixe', 's', ha='left')
save(fig, '11-138')
