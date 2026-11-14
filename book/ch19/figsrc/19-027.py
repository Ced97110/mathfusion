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
sh = [(0.09, 4, 0.09, 3, 'sujet')]
P = plane(ax, (30, 18), 9, (-2, 4), (-1, 3), shade=sh)
line(ax, [P(0, 0), P(4.6, 0)], 'resultat', lw=1.6); line(ax, [P(0, 0), P(0, 3.6)], 'resultat', lw=1.6)
p = P(3, 2)
line(ax, [p, P(3, 0)], 'resultat', dash=True); line(ax, [p, P(0, 2)], 'resultat', dash=True)
disc(ax, p[0], p[1], 1.4, 'sujet'); text(ax, p[0], p[1] + 4.2, '(3, 2)', 'sujet', 's')
text(ax, *P(1.2, 1.0), 'quadrant I', 'sujet', 's')
text(ax, P(3, 0)[0], P(3, 0)[1] - 4, '3 : positif', 'resultat', 's')
text(ax, 28, P(0, 2)[1] + 4, '2 : positif', 'resultat', 's', ha='right')
save(fig, '19-027')
