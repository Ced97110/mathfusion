import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ax.set_ylim(14, 90)  # même échelle (1 mm par unité) ; supprime le vide sous le contenu
# point de départ et ses deux ordres possibles
text(ax, 44, 87, '2 × 3²', 'encre', 'l', weight='bold')
arrow(ax, (40, 84), (24, 80.5), 'fixe')
arrow(ax, (48, 84), (64, 80.5), 'fixe')
# colonne gauche : le carré d'abord
text(ax, 22, 77, '3² devient 3 × 3', 'varie', 'm')
for x0 in (5, 24):
    for i in range(3):
        for j in range(3):
            box(ax, x0 + 3.5 * i, 54 + 3.5 * j, 3.5, 3.5, 'sujet', r=0.3)
    text(ax, x0 + 5.25, 59.25, '9', 'sujet', 's')
text(ax, 22, 47, '2 × 3 × 3', 'encre', 'm')
box(ax, 12, 30, 20, 8, 'resultat', label='= 18', size='l', weight='bold')
text(ax, 22, 24, 'le carré porte sur 3', 'resultat', 's')
# colonne droite : le produit d'abord
text(ax, 66, 77, "2 × 3 = 6 d'abord", 'limite', 'm')
for i in range(6):
    for j in range(6):
        box(ax, 57 + 3 * i, 46 + 3 * j, 3, 3, 'limite', r=0.3)
text(ax, 66, 42, '6 × 6', 'limite', 's')
box(ax, 56, 30, 20, 8, 'limite', label='= 36', size='l', weight='bold')
text(ax, 66, 24, 'le carré porte sur 6', 'limite', 's')
text(ax, 66, 19, "6 n'était pas sous le ²", 'limite', 's')
line(ax, [(44, 16), (44, 79)], 'fixe', dash=True)
save(fig, '04-058')
