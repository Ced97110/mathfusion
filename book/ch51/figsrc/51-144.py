import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
M = [([[1, 2], [3, 4]], 4, 'sujet'), ([[0, 0], [0, 0]], 34, 'fixe'), ([[1, 2], [3, 4]], 64, 'sujet')]
for mat, x0, role in M:
    for r in range(2):
        for c in range(2):
            box(ax, x0 + 9 * c, 18 - 9 * r + 4, 9, 9, role, label=str(mat[r][c]))
yc = 22.5
line(ax, [(25.5, yc), (30.5, yc)], 'encre', lw=1.2); line(ax, [(28, yc - 2.5), (28, yc + 2.5)], 'encre', lw=1.2)
line(ax, [(55.5, yc + 1.3), (60.5, yc + 1.3)], 'encre', lw=1.2); line(ax, [(55.5, yc - 1.3), (60.5, yc - 1.3)], 'encre', lw=1.2)
text(ax, 43, 9, 'matrice nulle', 'fixe', 's')
text(ax, 73, 9, 'inchangé', 'sujet', 's')
save(fig, '51-144')
