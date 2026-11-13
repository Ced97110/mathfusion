import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)

# carré de côté 3 : 9 carreaux jointifs ; le carreau haut-gauche est une pièce de côté 1
for i in range(3):
    for j in range(3):
        if (i, j) == (0, 2):
            box(ax, 10, 34, 7, 7, 'resultat', lw=0.6, r=0)
        else:
            box(ax, 10 + 7*i, 20 + 7*j, 7, 7, 'sujet', lw=0.6, r=0)
arrow(ax, (10, 16.5), (31, 16.5), 'varie', both=True)
text(ax, 20.5, 13.5, '3', 'varie', 's')
arrow(ax, (6.5, 20), (6.5, 41), 'varie', both=True)
text(ax, 4, 30.5, '3', 'varie', 's')

# cube de côté 2 : 8 petits cubes, le (0,0,1) en vert
O, U = (64, 20), 7
cells = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1) if (i, j, k) != (0, 0, 1)]
cubes(ax, cells, O, U, 'sujet')
cubes(ax, [(0, 0, 1)], O, U, 'resultat')

# trois arêtes du cube, décalées de 2 mm vers l'extérieur
arrow(ax, (65.0, 18.27), (77.12, 25.27), 'varie', both=True)
text(ax, 72, 20, '2', 'varie', 's')
arrow(ax, (63.0, 18.27), (50.88, 25.27), 'varie', both=True)
text(ax, 56, 20, '2', 'varie', 's')
arrow(ax, (78.5, 27), (78.5, 41), 'varie', both=True)
text(ax, 80.5, 34, '2', 'varie', 's')

text(ax, 20.5, 53, '3² = 9', 'resultat', 'l')
text(ax, 64, 53, '2³ = 8', 'resultat', 'l')
text(ax, 20.5, 8.5, '2 directions : 2 facteurs 3', 'encre', 's')
text(ax, 64, 8.5, '3 directions : 3 facteurs 2', 'encre', 's')
text(ax, 44, 3, 'pièces de côté 1, sans trou', 'resultat', 's')

save(fig, '04-007')
