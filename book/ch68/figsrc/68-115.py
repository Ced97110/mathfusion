import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
M = [[1, 0, 1], [0, 1, 1]]
e = [0, 1, 0]
X = [20 + 9 * c for c in range(3)]
text(ax, 8, 54, r'$e_2$', 'varie', 'm')
text(ax, 8, 32, '$H$', 'sujet', 'm')
for c in range(3):
    box(ax, X[c], 50, 9, 8, 'varie' if e[c] else 'fixe', label=str(e[c]))
    for r in range(2):
        box(ax, X[c], 36 - 9 * r, 9, 8, 'sujet', label=str(M[r][c]))
box(ax, X[1] - 1, 25, 11, 21, 'varie', fill=False, dash=True)
arrow(ax, (X[1] + 4.5, 49.5), (X[1] + 4.5, 46.5), 'varie')
arrow(ax, (50, 36), (63, 36), 'varie')
for r in range(2):
    box(ax, 64, 36 - 9 * r + 0, 9, 8, 'resultat', label=str(M[r][1]))
text(ax, 68.5, 20, 'colonne 2', 'resultat', 's')
save(fig, '68-115')
