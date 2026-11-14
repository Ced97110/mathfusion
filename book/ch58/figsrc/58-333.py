import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# tableau b_ij = b(e_i, e_j) : colonnes (2, 1) et (1, 3)
vals = [[2, 1], [1, 3]]  # vals[i][j] = b(e_{i+1}, e_{j+1})
c = 14.0
x0, y0 = 28, 12
text(ax, 44, 58, r'deux vecteurs $\to$ un nombre', 'sujet', 'm', weight='bold')
text(ax, x0 + c, y0 + 2 * c + 7, '2e vecteur', 'varie', 's')
text(ax, 13, y0 + c, '1er vecteur', 'varie', 's')
for j in range(2):
    text(ax, x0 + c * (j + 0.5), y0 + 2 * c + 2.5, rf'$e_{j+1}$', 'varie', 's')
for i in range(2):
    text(ax, x0 - 4, y0 + c * (1.5 - i), rf'$e_{i+1}$', 'varie', 's')
    for j in range(2):
        box(ax, x0 + c * j, y0 + c * (1 - i), c, c, 'sujet', label=str(vals[i][j]), size='l')
text(ax, x0 + c, y0 - 4, r'$b_{ij} = b(e_i, e_j)$', 'sujet', 's')
save(fig, '58-333')
