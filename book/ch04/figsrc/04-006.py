import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)

# écriture commune aux deux lecteurs
text(ax, 44, 82, '2 + 3 × 4', 'sujet', 'l', weight='bold')

# deux branches de lecture
arrow(ax, (40, 79), (24, 72), 'varie')
arrow(ax, (48, 79), (64, 72), 'varie')

# branche rouge : 2 + 3 d'abord, valeur 20, ne décrit pas l'achat
text(ax, 22, 68, '2 + 3 = 5', 'limite', 'm')
text(ax, 22, 62, '5 × 4 = 20', 'limite', 'm')
text(ax, 22, 55, "20 : pas l'achat", 'limite', 's')

# branche verte : 3 × 4 d'abord, valeur 14
text(ax, 66, 68, '3 × 4 = 12', 'resultat', 'm')
text(ax, 66, 62, '2 + 12 = 14', 'resultat', 'm')

# l'achat réel : 2 pains et 3 lots de 4 œufs
box(ax, 5, 16, 14, 5, 'autre')
box(ax, 5, 23, 14, 5, 'autre')
text(ax, 12, 10, '2 pains', 'autre', 's')
for x in (26, 44, 62):
    box(ax, x, 15, 14, 14, 'autre', fill=False, dash=True)
    for dx, dy in ((4.5, 4.5), (9.5, 4.5), (4.5, 9.5), (9.5, 9.5)):
        disc(ax, x + dx, 15 + dy, 2.2, 'autre')
text(ax, 51, 10, '3 lots de 4 = 12 œufs', 'autre', 's')

# seule la branche verte mène à l'achat
arrow(ax, (66, 58), (60, 40), 'resultat')
text(ax, 60, 37, "l'achat : 2 + 12 = 14 objets", 'resultat', 's')

text(ax, 44, 4, 'une ligne, une seule valeur : sinon deux achats', 'encre', 's')

save(fig, '04-006')
