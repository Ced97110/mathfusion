import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(94)

# titres de colonne
text(ax, 12, 88, 'on lit', 'sujet', 's')
text(ax, 50, 88, 'même test à chaque ligne', 'fixe', 's')

# bande grise : le même test derrière chaque ligne
box(ax, 39, 30, 22, 52, 'fixe')

# (y du centre de la ligne, égalité, test, taille du carré, y du bas de la grille)
rows = [(74, '√16 = 4', '4 × 4 = 16', 4, 70.1),
        (56, '√25 = 5', '5 × 5 = 25', 5, 50.6),
        (38, '√9 = 3', '3 × 3 = 9', 3, 34.9)]
for yc, eq, test, n, b in rows:
    text(ax, 12, yc, eq, 'sujet', 'l')
    text(ax, 29, yc, 'parce que', 'encre', 's')
    text(ax, 50, yc, test, 'resultat', 'l')
    for i in range(n):
        for j in range(n):
            box(ax, 66 + i * 2.2, b + j * 2.2, 1.9, 1.9, 'resultat', r=0.2)

# limite : 10 n'a pas de racine entière
text(ax, 22, 18, '√10 : aucun entier ne passe', 'limite', 's')
text(ax, 62, 18, '3 × 3 = 9 ; 4 × 4 = 16', 'limite', 's')

save(fig, '04-035')
