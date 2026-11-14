import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
M = [[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]
x0, y0, c = 8, 20, 13
for i in range(3):
    for j in range(3):
        v = M[i][j]; role = 'fixe' if i == j else ('sujet' if j > i else 'varie')
        box(ax, x0 + j * c, y0 + (2 - i) * c, c, c, role, label=str(v).replace('-', '−'), size='l')
text(ax, x0 + 1.5 * c, 62, r'$A^T=-A$', 'sujet', 'm')
text(ax, 66, 50, 'au-dessus', 'sujet', 's'); text(ax, 66, 40, 'en dessous :', 'varie', 's'); text(ax, 66, 36, 'les opposés', 'varie', 's')
text(ax, 66, 26, 'diagonale : 0', 'fixe', 's')
box(ax, 8, 4, 72, 11, 'limite'); text(ax, 44, 9.5, r'$\det A=-6+6=0$ : dégénérée', 'limite', 's')
save(fig, '71-200')
