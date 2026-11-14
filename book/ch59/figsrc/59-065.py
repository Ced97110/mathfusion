import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
text(ax, 44, 57, 'toute matrice mène à une matrice diagonale', 'encre', 's')
mat([['4', '6'], ['6', '4']], [['sujet'] * 2] * 2, 4, 24)
mat([['2', '0'], ['0', '10']], [['resultat', 'fixe'], ['fixe', 'resultat']], 62, 24)
arrow(ax, (28, 34.5), (58, 34.5), 'varie')
text(ax, 43, 39, 'lignes et colonnes', 'varie', 's')
text(ax, 14.5, 50, 'toute matrice', 'sujet', 's')
text(ax, 72.5, 50, 'forme diagonale', 'resultat', 's')
text(ax, 72.5, 17.5, 'zéros hors diagonale', 'fixe', 's')
box(ax, 10, 2, 68, 10, 'resultat', label=r'chaque nombre divise le suivant : $2\mid10$', size='s')
save(fig, '59-065')
