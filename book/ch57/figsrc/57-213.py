import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
# ligne 1 : matrice a gauche d'une colonne
cy = 76
text(ax, 4, cy + 13, 'colonne, matrice à gauche', 'fixe', 's', ha='left')
box(ax, 4, cy - 8, 26, 16, 'sujet', label='1  2\n0  3')
box(ax, 34, cy - 8, 14, 16, 'varie', label='4\n5')
text(ax, 53, cy, '=', 'encre', 'l')
box(ax, 58, cy - 8, 18, 16, 'resultat', label='14\n15')
# ligne 2 : ligne a gauche de la matrice
cy = 50
text(ax, 4, cy + 13, 'ligne, matrice à droite', 'fixe', 's', ha='left')
box(ax, 4, cy - 4.5, 26, 9, 'varie', label='4  5')
box(ax, 34, cy - 8, 26, 16, 'sujet', label='1  2\n0  3')
text(ax, 65, cy, '=', 'encre', 'l')
box(ax, 70, cy - 4.5, 16, 9, 'resultat', label='4  23')
# ligne 3 : colonne puis matrice, impossible
cy = 24
box(ax, 4, cy - 8, 14, 16, 'varie', label='4\n5')
box(ax, 22, cy - 8, 26, 16, 'sujet', label='1  2\n0  3')
text(ax, 53, cy, '=', 'encre', 'l')
box(ax, 58, cy - 8, 28, 16, 'limite', label='non défini')
save(fig, '57-213')
