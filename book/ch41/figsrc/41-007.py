import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Échelle 1 unité = 4 mm. Gauche : (4 ; 3) et (8 ; 6), pente 3/4. Droite : (4 ; 3) et (3 ; 4), longueur 5.
fig, ax = canvas(62)
u = 4.0
line(ax, [(44, 4), (44, 58)], 'fixe', lw=0.6, dash=True)
# Gauche
text(ax, 22, 56, 'pente 3/4 seule', 'sujet', 'm')
text(ax, 22, 50.5, 'longueur : 5 ou 10 ?', 'varie', 's')
O = (5, 12)
line(ax, [O, (40, 12)], 'fixe', lw=0.8)
arrow(ax, O, (O[0] + 8 * u, O[1] + 6 * u), 'varie', lw=1.2)
arrow(ax, O, (O[0] + 4 * u, O[1] + 3 * u), 'sujet', lw=1.4)
text(ax, O[0] + 4 * u + 1.5, O[1] + 3 * u - 3, '4 et 3', 'sujet', 's', ha='left')
text(ax, O[0] + 8 * u - 12, O[1] + 6 * u + 3, '8 et 6', 'varie', 's')
# Droite
text(ax, 66, 56, 'longueur 5 seule', 'sujet', 'm')
text(ax, 66, 50.5, 'pente : 3/4 ou 4/3 ?', 'varie', 's')
P = (50, 12)
line(ax, [P, (84, 12)], 'fixe', lw=0.8)
arrow(ax, P, (P[0] + 4 * u, P[1] + 3 * u), 'sujet', lw=1.4)
arrow(ax, P, (P[0] + 3 * u, P[1] + 4 * u), 'autre', lw=1.4)
text(ax, P[0] + 4 * u + 1.5, P[1] + 3 * u - 1, '4 et 3', 'sujet', 's', ha='left')
text(ax, P[0] + 3 * u - 3, P[1] + 4 * u + 3, '3 et 4', 'autre', 's')
save(fig, '41-007')
