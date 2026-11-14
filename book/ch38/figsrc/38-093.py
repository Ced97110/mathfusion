import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
# quatre points d'une chaîne ; chaque côté est un déplacement (longueur + direction)
P = [(8, 16), (30, 40), (52, 24), (78, 46)]
for i in range(3):
    arrow(ax, P[i], P[i + 1], 'sujet', lw=1.4)
for p in P:
    disc(ax, p[0], p[1], 1.1, 'sujet')
arrow(ax, P[0], P[3], 'resultat', lw=1.8)
text(ax, 8, 10, 'début', 'sujet', 's', ha='left')
text(ax, 78, 53, 'fin', 'sujet', 's')
text(ax, 17, 33, 'longueur', 'varie', 's', ha='right')
text(ax, 17, 29.5, 'et direction', 'varie', 's', ha='right')
text(ax, 44, 60, 'déplacements mis bout à bout', 'sujet', 'm')
text(ax, 44, 4, 'somme : un déplacement du début à la fin', 'resultat', 's')
save(fig, '38-093')
