import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'une équation = une ligne de $H$', 'encre', 'm')
M = [[1, 1, 1, 1], [1, 1, 0, 0]]
eqs = [r'$x_1+x_2+x_3+x_4=0$', r'$x_1+x_2=0$']
for r, (row, eq) in enumerate(zip(M, eqs)):
    y = 40 - 10 * r
    text(ax, 2, y + 4, eq, 'varie', 's', ha='left')
    arrow(ax, (36, y + 4), (49, y + 4), 'varie')
    for c, v in enumerate(row):
        box(ax, 50 + 9 * c, y, 9, 8, 'sujet' if v else 'fixe', label=str(v))
brace(ax, 50, 86, 18, 'sujet', label=r'$n=4$ colonnes')
text(ax, 44, 4, r'$m=2$ lignes : deux équations', 'sujet', 'm')
save(fig, '68-107')
