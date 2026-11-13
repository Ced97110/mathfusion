import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(46)
c = 5; ytop = 34
for k, x in enumerate((4, 34, 64)):
    for i in range(4):
        for j in range(4):
            if k == 0: r = 'fixe'
            elif k == 1: r = 'autre' if i == j else None
            else: r = 'sujet' if i // 2 == j // 2 else None
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None, r=0.3, lw=0.6)
text(ax, 14, 10, 'quelconque', 'fixe', 's')
text(ax, 44, 10, 'orthogonale', 'autre', 's')
text(ax, 74, 10, 'symplectique', 'sujet', 's')
text(ax, 14, 38, 'tout rempli', 'fixe', 's')
text(ax, 44, 38, 'diagonale', 'autre', 's')
text(ax, 74, 38, 'blocs $S$ puis zéros', 'sujet', 's')
text(ax, 64 + 5, ytop - 5, r'$S$', 'sujet', 'm'); text(ax, 64 + 15, ytop - 15, r'$S$', 'sujet', 'm')
save(fig, '71-099')
