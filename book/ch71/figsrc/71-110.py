import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(52)
box(ax, 4, 36, 20, 10, 'sujet', label='Pf = 3')
arrow(ax, (25, 41), (33, 41), 'varie')
text(ax, 29, 47.5, 'au carré', 'varie', 's')
box(ax, 33, 36, 16, 10, 'sujet', label=r'$3^2=9$')
text(ax, 54, 41, '=', 'resultat', 'l')
box(ax, 59, 36, 25, 10, 'autre', label='det = 9')
box(ax, 4, 16, 36, 10, 'resultat', label='produits et sommes')
box(ax, 46, 16, 38, 10, 'limite', label='division par 2', dash=True)
line(ax, [(47, 21), (83, 21)], 'limite', lw=1.2)
text(ax, 44, 8, 'vrai même si 2 = 0', 'resultat', 's')
save(fig, '71-110')
