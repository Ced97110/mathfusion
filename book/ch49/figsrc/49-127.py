import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, u = 14, 12, 9
box(ax, 3, 3, 82, 68, 'fixe', r=1.5)
text(ax, 44, 66, r'le plan $\mathbb{R}^2$ : tous les points', 'fixe', 's')
arrow(ax, (ox - 6, oy), (84, oy), 'encre', lw=0.8)
arrow(ax, (ox, oy - 6), (ox, 58), 'encre', lw=0.8)
px, py = ox + 3 * u, oy + 5 * u
line(ax, [(ox, oy), (px, oy), (px, py)], 'varie', lw=1.2, dash=True)
disc(ax, px, py, 2.4, 'sujet')
text(ax, px + 4, py + 1, r'$(3,\ 5)$', 'sujet', 'm', ha='left')
text(ax, (ox + px) / 2 + 12, oy - 4, '3 vers la droite', 'varie', 's')
text(ax, px + 3, (oy + py) / 2, '5 vers le haut', 'varie', 's', ha='left')
save(fig, '49-127')
