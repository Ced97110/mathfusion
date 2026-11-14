import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
M = [['a', 'b', 'c'], ['b', 'd', 'e'], ['c', 'e', 'f']]
role = {'b': 'varie', 'c': 'autre', 'e': 'resultat'}
c = 8
y0 = 30
for i in range(3):
    for j in range(3):
        v = M[i][j]
        box(ax, 6 + j * c, y0 + (2 - i) * c, c - 0.8, c - 0.8, role.get(v, 'sujet'), label=v)
line(ax, [(4.5, y0), (3.5, y0), (3.5, y0 + 23.2), (4.5, y0 + 23.2)], 'encre')
line(ax, [(29.6, y0), (30.6, y0), (30.6, y0 + 23.2), (29.6, y0 + 23.2)], 'encre')
text(ax, 17, 24, 'matrice symétrique', 'sujet', 's')
arrow(ax, (34, 42), (44, 42), 'varie')
text(ax, 66, 54, r'racines de $f$ : toutes réelles', 'resultat', 's')
arrow(ax, (46, 42), (86, 42), 'fixe', lw=0.8)
for x in (56, 66, 78):
    disc(ax, x, 42, 1.4, 'resultat')
arrow(ax, (66, 38), (66, 29), 'varie')
text(ax, 66, 24, 'forme de Jordan diagonale', 'resultat', 's')
save(fig, '60-267')
