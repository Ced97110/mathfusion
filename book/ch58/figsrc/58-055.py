import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
A = [[2, 1], [1, 3]]
cw, ch = 14.0, 11.0
x0, y0 = 28, 22
for i in range(2):
    for j in range(2):
        hl = (i == 1 and j == 1)
        box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, 'varie' if hl else 'sujet', label=str(A[i][j]), r=0.6, weight='bold' if hl else 'normal')
text(ax, x0 + cw * 0.5, y0 + 2 * ch + 4, 'colonne 1', 'fixe', 's')
text(ax, x0 + cw * 1.5, y0 + 2 * ch + 4, 'colonne 2', 'fixe', 's')
text(ax, x0 - 3, y0 + 1.5 * ch, 'ligne 1', 'fixe', 's', ha='right')
text(ax, x0 - 3, y0 + 0.5 * ch, 'ligne 2', 'fixe', 's', ha='right')
text(ax, 8, y0 + ch, r'$A$', 'sujet', 'xl', weight='bold')
text(ax, 44, 11, r'$a_{22}=3$ : ligne 2, colonne 2', 'varie', 's')
text(ax, 44, 3, r'$a_{ij}$ : ligne $i$, colonne $j$', 'encre', 's')
save(fig, '58-055')
