import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plane(ax, o, u, xr, yr, lx=None, ly=None, shade=(), names=True):
    lx = lx or {}; ly = ly or {}
    ox, oy = o
    P = lambda x, y: (ox + x * u, oy + y * u)
    for (xa, xb, ya, yb, role) in shade:
        ax.add_patch(Rectangle((ox + xa * u, oy + ya * u), (xb - xa) * u, (yb - ya) * u, fc=FILL[role], ec='none', zorder=1))
    for i in range(xr[0], xr[1] + 1):
        if i: ax.plot([ox + i * u] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.8, zorder=1.5)
    for j in range(yr[0], yr[1] + 1):
        if j: ax.plot([ox - 1, ox + 1], [oy + j * u] * 2, color=COL['fixe'], lw=0.8, zorder=1.5)
    arrow(ax, P(xr[0] - (0.4 if xr[0] < 0 else 0), 0), P(xr[1] + 0.6, 0), 'fixe', lw=0.9)
    arrow(ax, P(0, yr[0] - (0.4 if yr[0] < 0 else 0)), P(0, yr[1] + 0.6), 'fixe', lw=0.9)
    if names:
        text(ax, ox + (xr[1] + 0.6) * u, oy + 3, r'$x$', 'fixe', 's')
        text(ax, ox + 3, oy + (yr[1] + 0.6) * u, r'$y$', 'fixe', 's')
    for v, r in lx.items(): text(ax, ox + v * u, oy - 3.4, f'{v}'.replace('-', '\u2212'), r, 's')
    for v, r in ly.items(): text(ax, ox - 2.2, oy + v * u, f'{v}'.replace('-', '\u2212'), r, 's', ha='right')
    return P

fig, ax = canvas(84)
sh = [(0, 3, 0, 3, 'fixe'), (-3, 0, 0, 3, 'fixe'), (-3, 0, -3, 0, 'fixe'), (0, 3, -3, 0, 'fixe')]
sh = [(a + (0.09 if a == 0 else 0), b - (0.09 if b == 0 else 0), c + (0.09 if c == 0 else 0), d - (0.09 if d == 0 else 0), r) for a, b, c, d, r in sh]
P = plane(ax, (38, 42), 9, (-3, 3), (-3, 3), shade=sh)
for s, (a, b) in (('I', (1.9, 1.9)), ('II', (-1.9, 1.9)), ('III', (-1.9, -1.9)), ('IV', (1.9, -1.9))):
    text(ax, *P(a, b), s, 'sujet', 'l', weight='bold')
import math
R = 13
for k in range(4):
    a0, a1 = math.radians(50 + 90 * k), math.radians(130 + 90 * k)
    arrow(ax, (38 + R * math.cos(a0), 42 + R * math.sin(a0)), (38 + R * math.cos(a1), 42 + R * math.sin(a1)), 'varie', lw=1.2, curve=0.35)
text(ax, 44, 6, 'sens contraire des aiguilles', 'varie', 's')
save(fig, '19-026')
