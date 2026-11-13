import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(35)
M = [([[1, 2], [3, 4]], 4, 'sujet'), ([[5, 6], [7, 8]], 34, 'autre'), ([[6, 8], [10, 12]], 64, 'resultat')]
for mat, x0, role in M:
    for r in range(2):
        for c in range(2):
            hot = (r == 0 and c == 0)
            box(ax, x0 + 9 * c, 17.5 - 9 * r, 9, 9, 'varie' if hot else role, label=str(mat[r][c]))
text(ax, 28, 17.5, '+', 'encre', 'xl')
text(ax, 58, 17.5, '=', 'encre', 'xl')
save(fig, '51-143')
