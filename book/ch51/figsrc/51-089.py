import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(cx, role, vals, zeros):
    c = 9
    for i in range(2):
        for j in range(2):
            z = (i, j) in zeros
            box(ax, cx - c + j * c, 28 + (1 - i) * c - c + c, c, c, 'varie' if z else role, label=vals[2 * i + j], size='m')
mat(15, 'fixe', ['a', 'b', 'c', 'd'], [])
mat(44, 'sujet', ['1', '2', '0', '3'], [(1, 0)])
mat(73, 'autre', ['1', '0', '0', '3'], [(0, 1), (1, 0)])
for cx, t, n in [(15, 'quelconque', 'aucun zéro imposé'), (44, 'triangulaire supérieure', 'zéro en bas à gauche'), (73, 'diagonale', 'zéros hors diagonale')]:
    text(ax, cx, 50, t, 'encre', 's')
    text(ax, cx, 22, n, 'fixe', 's')
save(fig, '51-089')
