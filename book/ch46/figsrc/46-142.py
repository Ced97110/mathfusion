import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
ox, oy, u = 14, 10, 7
arrow(ax, (4, oy), (62, oy), 'fixe', lw=0.6); arrow(ax, (ox, 4), (ox, 47), 'fixe', lw=0.6)
disc(ax, ox, oy, u, 'resultat', fill=False)
zx, zy = ox + 3 * u, oy + 4 * u
line(ax, [(ox, oy), (zx, zy)], 'limite')
line(ax, [(zx, oy), (zx, zy)], 'limite', dash=True)
text(ax, zx, oy - 3, '3', 'limite', 's'); text(ax, zx + 2.6, oy + 2 * u, '4', 'limite', 's')
disc(ax, zx, zy, 1.0, 'limite'); text(ax, zx + 1.5, zy + 2.6, r'3 + 4$i$', 'limite', 's', ha='left')
for x, y, s, dx, dy in [(ox + u, oy, '1', 0, -3), (ox, oy + u, r'$i$', -2.4, 2.0)]:
    disc(ax, x, y, 1.0, 'resultat'); text(ax, x + dx, y + dy, s, 'resultat', 's')
text(ax, ox - 2.6, oy - 3, 'O', 'fixe', 's')
text(ax, 50, 22, r'1 et $i$ : $|z| = 1$', 'resultat', 's', ha='left')
text(ax, 50, 30, r'3 + 4$i$ : $|z| = 5$', 'limite', 's', ha='left')
save(fig, '46-142')
