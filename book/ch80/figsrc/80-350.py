import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
box(ax, 4, 14, 34, 38, 'sujet')
text(ax, 9, 47, r'$A$', 'sujet', 'm')
for i in range(5):
    for j in range(3):
        disc(ax, 9 + 6 * i, 21 + 8 * j, 1.9, 'fixe')
text(ax, 21, 8, 'multiples de 2 de 1 à 30', 'fixe', 's')
arrow(ax, (40, 33), (49, 33), 'varie')
text(ax, 66, 45, r'$|A|$', 'sujet', 'xl')
text(ax, 66, 32, r'$|A|=15$', 'resultat', 'l')
text(ax, 66, 21, "nombre d'éléments", 'resultat', 's')
text(ax, 66, 17, r'de $A$', 'resultat', 's')
save(fig, '80-350')
