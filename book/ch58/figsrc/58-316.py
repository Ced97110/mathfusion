import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 4.2
# gauche : det = 0
ox, oy = 22, 44
p = lambda x, y: (ox + x * u, oy + y * u)
text(ax, 22, 68, 'colonnes (1, 2), (2, 4)', 'encre', 's')
text(ax, 22, 63, 'det = 1·4 − 2·2 = 0', 'varie', 's')
line(ax, [p(-1.5, -3), p(1.5, 3)], 'resultat', lw=1.8)
disc(ax, ox, oy, 1.2, 'sujet')
text(ax, ox + 9, oy - 6, 'image : droite', 'resultat', 's')
box(ax, 2, 6, 20, 9, 'sujet', label='noyau 1', size='s')
box(ax, 22, 6, 20, 9, 'resultat', label='image 1', size='s')
text(ax, 22, 19, '1 + 1 = 2', 'encre', 's')
# droite : det = 5
ox2 = 66
text(ax, 66, 68, 'colonnes (2, 1), (1, 3)', 'encre', 's')
text(ax, 66, 63, 'det = 2·3 − 1·1 = 5', 'resultat', 's')
ax.add_patch(Rectangle((ox2 - 17, oy - 15), 34, 30, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=1))
disc(ax, ox2, oy, 1.2, 'sujet')
text(ax, ox2, oy - 8, 'image : tout le plan', 'resultat', 's')
box(ax, 46, 6, 6, 9, 'sujet', label='0', size='s')
box(ax, 52, 6, 34, 9, 'resultat', label='image 2', size='s')
text(ax, 66, 19, '0 + 2 = 2', 'encre', 's')
text(ax, ox2, oy + 5, 'noyau {0} : O', 'sujet', 's')
save(fig, '58-316')
