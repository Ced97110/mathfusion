import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(x, y, vals, roles, c=9):
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            box(ax, x + j * c, y + (1 - i) * c, c - 0.8, c - 0.8, roles[i][j], label=v)
    line(ax, [(x - 1, y), (x - 2, y), (x - 2, y + 2 * c - 0.8), (x - 1, y + 2 * c - 0.8)], 'encre')
    line(ax, [(x + 2 * c - 0.2, y), (x + 2 * c + 0.8, y), (x + 2 * c + 0.8, y + 2 * c - 0.8), (x + 2 * c - 0.2, y + 2 * c - 0.8)], 'encre')
text(ax, 44, 61, r'$f=(\lambda-2)^2$ pour les deux', 'resultat', 's')
mat(8, 34, [['2', '1'], ['0', '2']], [['sujet', 'sujet'], ['fixe', 'sujet']])
mat(62, 34, [['2', '0'], ['0', '2']], [['autre', 'fixe'], ['fixe', 'autre']])
text(ax, 39, 43, 'non semblables', 'limite', 's')
text(ax, 17, 26, r'$(\lambda-2)^2$', 'sujet', 's')
text(ax, 71, 26, r'$\lambda-2,\ \lambda-2$', 'autre', 's')
text(ax, 44, 14, 'listes de facteurs invariants', 'fixe', 's')
save(fig, '60-266')
