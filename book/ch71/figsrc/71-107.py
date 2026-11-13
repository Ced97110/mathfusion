import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(46)
mat(ax, 5, 34, [['0', '3'], [r'$-3$', '0']], 10, [['fixe', 'resultat'], ['fixe', 'fixe']])
arrow(ax, (26, 29), (36, 29), 'resultat')
box(ax, 36, 24, 22, 10, 'resultat', label='Pf = 3')
arrow(ax, (59, 29), (67, 29), 'varie')
text(ax, 63, 37, 'au carré', 'varie', 's')
box(ax, 67, 24, 18, 10, 'sujet', label='det = 9')
text(ax, 47, 19, 'lu sur la matrice', 'resultat', 's')
text(ax, 76, 19, 'déterminant', 'sujet', 's')
save(fig, '71-107')
