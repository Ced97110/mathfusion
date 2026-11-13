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
fig, ax = canvas(80)
for i in range(3):
    for j in range(3):
        box(ax, 8 + 4 * i, 62 + 4 * j, 4, 4, 'sujet', r=0.3)
text(ax, 30, 68, r'$r^2=3^2=9$', 'sujet', 'm', ha='left')
disc(ax, 14, 50, 6, 'sujet'); line(ax, [(14, 50), (20, 50)], 'sujet', lw=1.0)
text(ax, 17, 47.8, r'$r$', 'sujet', 's')
text(ax, 30, 50, r'aire de la base : $9\pi$', 'sujet', 'm', ha='left')
cyl(ax, 14, 27.5, 5, 1.8, 9, 'autre')
text(ax, 30, 32, r'$\times\,6$ : cylindre $54\pi$', 'autre', 'm', ha='left')
cone(ax, 14, 9.5, 5, 1.8, 9, 'sujet')
text(ax, 30, 14, r'$\div\,3$ : cône $18\pi\approx56{,}52$', 'resultat', 'm', ha='left')
for ya, yb in ((60.8, 57.2), (43, 40.5), (24.5, 20.5)):
    arrow(ax, (14, ya), (14, yb), 'varie')
save(fig, '11-135')
