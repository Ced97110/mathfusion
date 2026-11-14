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
fig, ax = canvas(56)
cx, r, e, y0, h = 28, 13, 4, 10, 30
cyl(ax, cx, y0, r, e, h, 'sujet', layers=10)
line(ax, [(cx, y0 + h), (cx + r, y0 + h)], 'sujet', lw=1.0)
text(ax, cx + r / 2, y0 + h + 2.3, r'$r$', 'sujet', 's')
arrow(ax, (10, y0), (10, y0 + h), 'varie', both=True)
text(ax, 6, y0 + h / 2, r'$h$', 'varie', 'm')
text(ax, 50, 46, 'base : un disque', 'sujet', 's', ha='left')
arrow(ax, (49, 45.2), (cx + r - 2, y0 + h + 1.5), 'fixe')
text(ax, 50, 22, '10 couches\nidentiques', 'sujet', 's', ha='left')
arrow(ax, (49, 24), (cx + r + 0.6, 24), 'fixe')
save(fig, '11-131')
