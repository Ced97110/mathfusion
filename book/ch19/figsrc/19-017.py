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

fig, ax = canvas(62)
P = plane(ax, (18, 14), 11, (0, 4), (0, 3), lx={3: 'sujet'}, ly={2: 'varie'})
p = P(3, 2)
line(ax, [p, P(3, 0)], 'sujet', dash=True); line(ax, [p, P(0, 2)], 'varie', dash=True)
disc(ax, p[0], p[1], 1.3, 'sujet'); text(ax, p[0] + 2.6, p[1] + 2.6, r'$P$', 'sujet', 'm')
text(ax, 48, 6, 'premier nombre : 3', 'sujet', 's')
text(ax, 26, 52, 'second nombre : 2', 'varie', 's', ha='left')
text(ax, 70, 42, r'$P\,(3,\ 2)$', 'resultat', 'l')
save(fig, '19-017')
