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
fig, ax = canvas(76)
cy = 40
box(ax, 8, 62, 72, 9, 'resultat', label=r'$V\div r^3\approx4{,}19$ : toujours', size='m')
for rr, cx, v in ((1, 11, '4,19'), (2, 33, '33,49'), (3, 65, '113,04')):
    R = 5 * rr
    disc(ax, cx, cy, R, 'sujet'); equator(ax, cx, cy, R)
    text(ax, cx, 20, f'$r={rr}$', 'varie', 's')
    text(ax, cx, 14, f'$r^3={rr**3}$', 'varie', 's')
    text(ax, cx, 8, f'V ≈ {v}', 'sujet', 's')
save(fig, '11-137')
