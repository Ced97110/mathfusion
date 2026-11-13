import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
O, U = (24, 12), 8
cells = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
cubes(ax, cells, O, U, 'sujet')

P = lambda x, y, z: iso(x, y, z, O, U)
line(ax, [P(0,0,0), P(2,0,0)], 'varie', lw=1.4)
line(ax, [P(0,0,0), P(0,2,0)], 'varie', lw=1.4)
line(ax, [P(2,0,0), P(2,0,2)], 'varie', lw=1.4)
text(ax, 36, 11, 'longueur 2', 'varie', 's')
text(ax, 12, 11, 'largeur 2', 'varie', 's')
text(ax, 40, 28, 'hauteur 2', 'varie', 's', ha='left')

text(ax, 24, 50, '2 × 2 × 2 = 8', 'resultat', 'm')
text(ax, 24, 5, '3 facteurs = 3 directions', 'encre', 's')

text(ax, 70, 50, '2 × 2 × 2 × 2 = 16', 'resultat', 'm')
box(ax, 54, 14, 32, 28, 'limite', fill=False, dash=True)
# les trois directions de l'espace (mêmes axes que la caisse), puis la 4e : aucune place
Q = lambda x, y, z: iso(x, y, z, (70, 18), 6)
arrow(ax, Q(0,0,0), Q(1.6,0,0), 'varie', lw=1.0)
arrow(ax, Q(0,0,0), Q(0,1.6,0), 'varie', lw=1.0)
arrow(ax, Q(0,0,0), Q(0,0,1.9), 'varie', lw=1.0)
text(ax, 70, 38.5, 'aucun dessin', 'limite', 'm')
a4 = ax.add_patch(FancyArrowPatch((70, 18), (82, 31), arrowstyle='-|>', mutation_scale=7, lw=1.0,
                  color=COL['limite'], linestyle='--', shrinkA=0, shrinkB=0, zorder=4))
text(ax, 80, 34, '4e ?', 'limite', 's')
text(ax, 70, 5, '16 est juste, sans figure', 'limite', 's')

save(fig, '04-002')
