import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(48)
mat(ax, 6, 42, [['0', r'$a$'], [r'$-a$', '0']], 10, [['fixe', 'resultat'], ['varie', 'fixe']])
text(ax, 36, 38, r'Pf $=a$', 'resultat', 'l', ha='left')
text(ax, 36, 31, r'$0\times 0=0$', 'fixe', 'm', ha='left')
text(ax, 36, 25, r'$-\,a\times(-a)=a^2$', 'varie', 'm', ha='left')
text(ax, 36, 18, r'det $=a^2$', 'sujet', 'l', ha='left')
text(ax, 44, 8, r'cas $a=3$ : Pf $=3$, det $=9$', 'encre', 's')
save(fig, '71-108')
