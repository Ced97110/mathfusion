import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 14, 10, 16
arrow(ax, (ox, oy), (84, oy), 'fixe'); arrow(ax, (ox, oy), (ox, 61), 'fixe')
px, py = ox + 3 * u, oy + 2 * u
line(ax, [(px, oy), (px, py)], 'fixe', dash=True); line(ax, [(ox, py), (px, py)], 'fixe', dash=True)
for k in range(1, 5): ax.plot([ox + k * u] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.8)
for k in range(1, 4): ax.plot([ox - 1, ox + 1], [oy + k * u] * 2, color=COL['fixe'], lw=0.8)
text(ax, px, oy - 4, '3', 'fixe', 's'); text(ax, ox - 4, py, '2', 'fixe', 's')
disc(ax, px, py, 1.8, 'sujet')
text(ax, px - 3, py + 5, 'point (3 ; 2)', 'sujet', 's', ha='right')
text(ax, px + 3, py - 8, 'nombre 3 + 2i', 'resultat', 's', ha='left')
save(fig, '61-152')
