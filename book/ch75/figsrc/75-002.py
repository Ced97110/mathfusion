import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
f = numberline(ax, 6, 60, 64, 0, 6, every=3)
text(ax, 74, 64, 'rail', 'fixe', 's')
disc(ax, f(3), 67.5, 2.4, 'sujet'); disc(ax, f(3), 67.5, 1.2, 'autre')
text(ax, 44, 74, 'même endroit du rail', 'fixe', 's', ha='left')
text(ax, 44, 51, 'plan des phases', 'encre', 'm')
ox, oy, u = 14, 8, 8
arrow(ax, (ox, oy), (ox + 6 * u + 4, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + 4 * u + 4), 'fixe', lw=0.8)
text(ax, ox + 6 * u + 4, oy - 3, r'$x$', 'fixe', 's'); text(ax, ox - 4, oy + 4 * u + 4, r'$v$', 'fixe', 's')
px = ox + 3 * u
line(ax, [(px, oy), (px, oy + 4 * u)], 'fixe', dash=True)
disc(ax, px, oy + u, 1.8, 'sujet'); disc(ax, px, oy + 4 * u, 1.8, 'autre')
text(ax, px + 3, oy + u, r'$v$ = 1', 'sujet', 's', ha='left'); text(ax, px + 3, oy + 4 * u, r'$v$ = 4', 'autre', 's', ha='left')
text(ax, px, oy - 3, '3', 'fixe', 's')
save(fig, '75-002')
