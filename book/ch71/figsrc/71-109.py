import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(50)
c = 7; ytop = 44; x0 = 4
roles = {(0, 1): 'sujet', (2, 3): 'sujet', (0, 2): 'autre', (1, 3): 'autre', (0, 3): 'varie', (1, 2): 'varie'}
vals = {(0, 1): '1', (0, 2): '3', (0, 3): '2', (1, 2): '1', (1, 3): '2', (2, 3): '2'}
for i in range(4):
    for j in range(4):
        r = roles.get((i, j))
        box(ax, x0 + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=(r is not None or i == j), r=0.3, lw=0.6,
            label=vals.get((i, j)))
text(ax, 18, 11, 'coefficients au-dessus', 'fixe', 's')
text(ax, 40, 38, r'$+\;1\times 2=2$', 'sujet', 'm', ha='left')
text(ax, 40, 30, r'$-\;3\times 2=6$', 'autre', 'm', ha='left')
text(ax, 40, 22, r'$+\;2\times 1=2$', 'varie', 'm', ha='left')
text(ax, 40, 12, r'Pf $=2-6+2=-2$', 'resultat', 'm', ha='left')
save(fig, '71-109')
