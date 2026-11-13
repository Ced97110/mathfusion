import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(72)
text(ax, 14, 70, 'alternée 2 × 2', 'sujet', 's')
mat(ax, 5, 66, [['0', '3'], [r'$-3$', '0']], 9, [['sujet'] * 2] * 2)
text(ax, 28, 61, 'rang 2 : pair', 'resultat', 's', ha='left')
text(ax, 28, 53, r'déterminant $9=3^2$', 'resultat', 's', ha='left')
text(ax, 17, 44, 'alternée 3 × 3', 'sujet', 's')
mat(ax, 5, 40, [['', '', ''], ['', '', ''], ['', '', '']], 7,
    [['sujet', 'sujet', 'fixe'], ['sujet', 'sujet', 'fixe'], ['fixe', 'fixe', 'fixe']])
text(ax, 30, 33, 'rang au plus 2', 'resultat', 's', ha='left')
text(ax, 30, 25, 'déterminant 0', 'resultat', 's', ha='left')
save(fig, '71-104')
