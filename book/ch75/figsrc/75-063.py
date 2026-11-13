import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 14, 31, 9
arrow(ax, (6, oy), (80, oy), 'fixe', lw=0.8); arrow(ax, (ox, 4), (ox, 58), 'fixe', lw=0.8)
zx = ox + 3 * u
disc(ax, zx, oy + 2 * u, 1.8, 'sujet'); disc(ax, zx, oy - 2 * u, 1.8, 'resultat')
line(ax, [(zx, oy - 2 * u), (zx, oy + 2 * u)], 'fixe', dash=True)
text(ax, zx + 3, oy + 2 * u + 3, r'$z=3+2i$', 'sujet', 'm', ha='left')
text(ax, zx + 3, oy - 2 * u - 3, r'$\bar{z}=3-2i$', 'resultat', 'm', ha='left')
arrow(ax, (zx - 6, oy + 2 * u - 3), (zx - 6, oy - 2 * u + 3), 'varie', curve=0)
text(ax, zx + 3, oy + 3, '3', 'fixe', 's', ha='left')
text(ax, ox - 3, oy + 2 * u, '2', 'fixe', 's'); text(ax, ox - 3, oy - 2 * u, '−2', 'fixe', 's')
text(ax, 46, oy - 5, 'signe changé', 'varie', 's', ha='right')
save(fig, '75-063')
