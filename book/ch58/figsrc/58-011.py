import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# deux modules : l'un a une base (libre), l'autre n'en a pas
text(ax, 21, 60, r'couples d’entiers $\mathbb{Z}^{(2)}$', 'sujet', 's', weight='bold')
text(ax, 67, 60, 'horloge à 2 heures', 'autre', 's', weight='bold')
# gauche : axes et deux flèches e1, e2
ox, oy, u = 9, 20, 18
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.6)
arrow(ax, (ox, oy), (ox, oy + u), 'autre', lw=1.6)
disc(ax, ox, oy, 1.0, 'encre')
text(ax, ox + u + 3, oy + 3, r'$e_1$', 'sujet', 'm')
text(ax, ox - 4, oy + u + 1, r'$e_2$', 'autre', 'm')
text(ax, 21, 50, 'deux sacs types', 'sujet', 's')
# droite : horloge à 2 heures
cx, cy, r = 67, 38, 11
disc(ax, cx, cy, r, 'fixe', fill=False, lw=1.0)
disc(ax, cx, cy + r, 2.2, 'autre', label='0', size='s')
disc(ax, cx, cy - r, 2.2, 'autre', label='1', size='s')
text(ax, cx, cy, 'pas de base', 'limite', 's')
box(ax, 4, 4, 34, 9, 'resultat', label='a une base : libre', size='s', weight='bold')
box(ax, 50, 4, 34, 9, 'limite', label='sans base : pas libre', size='s', weight='bold')
save(fig, '58-011')
