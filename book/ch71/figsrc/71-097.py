import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(52)
mat(ax, 6, 40, [['0', '1'], [r'$-1$', '0']], 11, [['sujet', 'fixe'], ['fixe', 'sujet']])
mat(ax, 60, 40, [['0', r'$-1$'], ['1', '0']], 11, [['sujet', 'varie'], ['varie', 'sujet']])
arrow(ax, (31, 29), (57, 29), 'varie')
text(ax, 44, 33, 'transposée', 'varie', 's')
text(ax, 17, 44, r'$A$', 'sujet', 'l')
text(ax, 71, 44, r'$A^T=-A$', 'sujet', 'l')
text(ax, 17, 12, 'diagonale : 0', 'sujet', 's')
text(ax, 71, 12, 'signes changés', 'varie', 's')
save(fig, '71-097')
