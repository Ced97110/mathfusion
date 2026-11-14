import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(52)
o = (44, 8); u = 2.2
P = lambda a, b, cz=0: iso(a, b, cz, o, u)
poly(ax, [P(0, 0), P(7, 0), P(7, 7), P(0, 7)], 'sujet')
text(ax, 44, 5, r'plan $(u_1, v_1)$', 'sujet', 's')
arrow(ax, P(0, 0), P(3, 5, 7), 'fixe', lw=1.1)
text(ax, 38, 38, r'$x=(3,\,5,\,7)$', 'fixe', 'm', ha='right')
arrow(ax, P(0, 0), P(3, 5, 0), 'varie', lw=1.3)
text(ax, 31.5, 20, 'part dans le plan', 'varie', 's', ha='right')
line(ax, [P(3, 5, 0), P(3, 5, 7)], 'varie', dash=True)
arrow(ax, (44, 8), (44, 8 + 7 * u), 'resultat', lw=1.6)
text(ax, 47, 26, r'$y=(0,\,0,\,7)$', 'resultat', 'm', ha='left')
save(fig, '71-102')
