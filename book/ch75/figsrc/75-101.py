import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
M = [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]
x0, y0, c = 14, 20, 12
for i in range(3):
    for j in range(3):
        role = 'varie' if (i, j) in ((0, 1), (1, 0)) else ('sujet' if i == j else 'fixe')
        box(ax, x0 + j * c, y0 + (2 - i) * c, c, c, role, label=str(M[i][j]).replace('-', '−'), size='l')
text(ax, x0 - 4, y0 + 18, r'$A$', 'sujet', 'l')
text(ax, x0 + 18, y0 + 3 * c + 6, 'ligne $i$, colonne $j$', 'fixe', 's')
# mirror arrow across the diagonal between cells (0,1) and (1,0)
a = (x0 + 1.5 * c, y0 + 2.5 * c); b = (x0 + 0.5 * c, y0 + 1.5 * c)
arrow(ax, (a[0] - 3, a[1] - 3), (b[0] + 3, b[1] + 3), 'varie', curve=0.0, both=True)
text(ax, 66, 54, r'$B(e_i,\,e_j)=1$', 'varie', 's')
text(ax, 66, 46, r'$B(e_j,\,e_i)=-1$', 'varie', 's')
text(ax, 62, 33, 'diagonale : 0', 'sujet', 's')
text(ax, 62, 10, r'$A^t=-A$', 'resultat', 'l')
save(fig, '75-101')
