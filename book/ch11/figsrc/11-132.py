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
fig, ax = canvas(62)
k, r, e, y0 = 1.3, 5.2, 1.8, 12
text(ax, 44, 58, r'$V=\pi r^2 h$', 'sujet', 'l')
text(ax, 44, 51, 'même base : aire ≈ 50,24', 'fixe', 's')
for cx, hc, lay, v in ((16, 5, 1, '251,2'), (44, 10, 2, '502,4'), (72, 20, 4, '1 004,8')):
    cyl(ax, cx, y0, r, e, hc * k, 'sujet', layers=lay)
    text(ax, cx, y0 + hc * k + 5.5, f'$h={hc}$', 'varie', 'm')
    text(ax, cx, 6, f'V ≈ {v}', 'resultat', 's')
save(fig, '11-132')
