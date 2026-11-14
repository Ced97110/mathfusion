import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'degré 3 : au plus 3 racines', 'encre', 's')
text(ax, 4, 53, 'corps infini', 'sujet', 's', ha='left')
text(ax, 84, 53, 'vert = racine', 'resultat', 's', ha='right')
for i in range(22):
    disc(ax, 6 + i * 3.6, 44, 1.5, 'resultat' if i in (3, 10, 17) else 'fixe')
text(ax, 44, 35, 'seulement 3 racines au plus', 'fixe', 's')
text(ax, 4, 25, 'corps à 3 éléments', 'autre', 's', ha='left')
for x in (30, 44, 58):
    disc(ax, x, 16, 1.5, 'resultat')
text(ax, 44, 8, 'les 3 éléments : 3 racines', 'resultat', 's')
save(fig, '55-017')
