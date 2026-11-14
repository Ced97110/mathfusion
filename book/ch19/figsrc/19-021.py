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

fig, ax = canvas(80)
text(ax, 4, 74, 'Élève 1 : (3, 2)', 'sujet', 'm', ha='left')
text(ax, 4, 68, 'Élève 2 : (2, 3)', 'autre', 'm', ha='left')
P = plane(ax, (14, 8), 11, (0, 4), (0, 4), lx={3: 'sujet', 2: 'autre'}, ly={2: 'sujet', 3: 'autre'})
for (a, b), r in (((3, 2), 'sujet'), ((2, 3), 'autre')):
    p = P(a, b)
    line(ax, [p, P(a, 0)], r, dash=True); line(ax, [p, P(0, b)], r, dash=True)
    disc(ax, p[0], p[1], 1.4, r)
text(ax, 74, 36, 'deux points', 'limite', 's'); text(ax, 74, 31, 'différents', 'limite', 's')
save(fig, '19-021')
