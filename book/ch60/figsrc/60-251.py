import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(x, y, vals, roles, c=9):
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            box(ax, x + j * c, y + (1 - i) * c, c - 0.8, c - 0.8, roles[i][j], label=v)
    line(ax, [(x - 1, y), (x - 2, y), (x - 2, y + 2 * c - 0.8), (x - 1, y + 2 * c - 0.8)], 'encre')
    line(ax, [(x + 2 * c - 0.2, y), (x + 2 * c + 0.8, y), (x + 2 * c + 0.8, y + 2 * c - 0.8), (x + 2 * c - 0.2, y + 2 * c - 0.8)], 'encre')
mat(8, 26, [['2', '0'], ['0', '2']], [['sujet', 'fixe'], ['fixe', 'sujet']])
mat(52, 26, [['2', '1'], ['0', '2']], [['autre', 'limite'], ['fixe', 'autre']])
text(ax, 17, 52, 'diagonalisable', 'resultat', 'm')
text(ax, 61, 52, 'pas diagonalisable', 'limite', 'm')
text(ax, 17, 17, 'tous blocs de taille 1', 'resultat', 's')
text(ax, 61, 17, 'un bloc de taille 2', 'limite', 's')
save(fig, '60-251')
