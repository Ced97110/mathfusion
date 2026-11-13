import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 7
for i in range(2):
    for j in range(3):
        poly(ax, [(6+i*s, 22+j*s), (6+(i+1)*s, 22+j*s), (6+(i+1)*s, 22+(j+1)*s), (6+i*s, 22+(j+1)*s)], 'sujet')
text(ax, 13, 49, 'aire orientée', 'sujet', 's'); text(ax, 13, 13, r'$2\times3=6$', 'sujet', 's')
text(ax, 13, 54, 'dimension 2', 'fixe', 's')
cubes(ax, [(i, j, k) for i in range(2) for j in range(3) for k in range(4)], (62, 12), 5, 'sujet')
text(ax, 64, 54, 'volume orienté', 'resultat', 's'); text(ax, 64, 4.5, r'$2\times3\times4=24$', 'resultat', 's')
arrow(ax, (25, 35), (44, 35), 'varie'); text(ax, 35, 39, 'dimension 3', 'varie', 's')
text(ax, 35, 31, 'même objet', 'varie', 's')
save(fig, '71-219')
