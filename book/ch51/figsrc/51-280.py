import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 22, 68, 'cadran à 7 heures', 'sujet', 's')
text(ax, 66, 68, 'quatre tableaux', 'autre', 's')
for i in range(7):
    disc(ax, 5 + i * 6, 52, 2.4, 'sujet')
text(ax, 22, 42, '7 éléments', 'sujet', 'm')
for i in range(2):
    for j in range(2):
        disc(ax, 60 + i * 8, 56 - j * 8, 2.8, 'autre')
text(ax, 66, 42, '4 éléments', 'autre', 'm')
text(ax, 22, 30, '$7 = 7^1$', 'sujet', 'l')
text(ax, 66, 30, '$4 = 2^2$', 'autre', 'l')
text(ax, 22, 20, 'caractéristique 7', 'sujet', 's')
text(ax, 66, 20, 'caractéristique 2', 'autre', 's')
box(ax, 4, 3, 80, 11, 'resultat', label='taille = puissance de la caractéristique', size='s')
save(fig, '51-280')
