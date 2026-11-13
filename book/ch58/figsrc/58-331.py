import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 5.6
# gauche : la base donne des coordonnées
ox, oy = 8, 20
arrow(ax, (ox, oy), (ox + 6.2 * u, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox, oy + 5.2 * u), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.8)
arrow(ax, (ox, oy), (ox, oy + u), 'sujet', lw=1.8)
text(ax, ox + u / 2, oy - 3.2, r'$e_1$', 'sujet', 's')
text(ax, ox - 2.8, oy + u / 2 + 1.5, r'$e_2$', 'sujet', 's')
px, py = ox + 5 * u, oy + 4 * u
line(ax, [(px, oy), (px, py)], 'fixe', dash=True, lw=0.6)
line(ax, [(ox, py), (px, py)], 'fixe', dash=True, lw=0.6)
disc(ax, px, py, 1.3, 'varie')
text(ax, px, oy - 3.2, '5', 'varie', 's')
text(ax, ox - 2.8, py, '4', 'varie', 's')
text(ax, px - 2, py + 3.5, '(5, 4)', 'varie', 's', ha='right')
text(ax, 21, 58, 'Base', 'sujet', 'l', weight='bold')
text(ax, 21, 6, 'sans base : pas de matrice', 'sujet', 's')
# droite : la somme directe coupe
ox2 = 52
arrow(ax, (ox2, oy), (ox2 + 6.2 * u * 0.62, oy), 'fixe', lw=0.7)
arrow(ax, (ox2, oy), (ox2, oy + 5.2 * u), 'fixe', lw=0.7)
qx, qy = ox2 + 5 * u * 0.62, oy + 4 * u
arrow(ax, (ox2, oy), (qx, oy), 'sujet', lw=1.8)
arrow(ax, (ox2, oy), (ox2, qy), 'autre', lw=1.8)
line(ax, [(qx, oy), (qx, qy)], 'fixe', dash=True, lw=0.6)
line(ax, [(ox2, qy), (qx, qy)], 'fixe', dash=True, lw=0.6)
disc(ax, qx, qy, 1.3, 'varie')
text(ax, qx - 1, qy + 3.5, '(5, 4)', 'varie', 's', ha='right')
text(ax, qx, oy - 3.2, '(5, 0)', 'sujet', 's')
text(ax, ox2 + 2, qy - 4.2, '(0, 4)', 'autre', 's', ha='left')
text(ax, 66, 58, 'Somme directe', 'sujet', 'l', weight='bold')
text(ax, 66, 6, r'sans $\oplus$ : pas de coupure', 'sujet', 's')
save(fig, '58-331')
