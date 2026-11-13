import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(90)

# séparation entre les deux voisins comparés
line(ax, [(44, 33), (44, 88)], 'fixe', lw=0.5)

# colonne gauche : racine carrée, deux facteurs égaux
text(ax, 17, 85, 'racine carrée', 'autre', 'm')
text(ax, 17, 79, 'deux facteurs égaux', 'autre', 's')
for x, y in [(10, 57), (17, 57), (10, 50), (17, 50)]:
    box(ax, x, y, 7, 7, 'autre', r=0.3)
text(ax, 17, 42, 'côté 2', 'varie', 's')
text(ax, 17, 36.5, '2 × 2 = 4 : une aire', 'autre', 's')

# colonne droite : racine cubique, trois facteurs égaux
text(ax, 66, 85, 'racine cubique', 'sujet', 'm')
text(ax, 66, 79, 'trois facteurs égaux', 'sujet', 's')
cells = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
cubes(ax, cells, (66, 46), 7, 'sujet')
text(ax, 66, 42, 'côté 2', 'varie', 's')
text(ax, 66, 36.5, '2 × 2 × 2 = 8 : un volume', 'sujet', 's')

# la racine carrée de 8 n'est pas 2 ; la racine cubique de 27 est 3
text(ax, 44, 25, 'racine carrée de 8 : pas 2', 'limite', 's')
text(ax, 22, 15, 'racine cubique de 27 : 3', 'resultat', 's')
text(ax, 22, 8, '3 × 3 × 3 = 27', 'resultat', 's')
text(ax, 66, 15, '27 ÷ 3 = 9 : autre chose', 'limite', 's')

save(fig, '04-037')
