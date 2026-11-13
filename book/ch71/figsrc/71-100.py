import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(58)
o = (44, 12); u = 20
P = lambda a, b, cz=0: iso(a, b, cz, o, u)
poly(ax, [P(0, 0), P(1.2, 0), P(1.2, 1.2), P(0, 1.2)], 'sujet')
arrow(ax, P(0, 0), P(1.2, 0), 'sujet', lw=1.3)
arrow(ax, P(0, 0), P(0, 1.2), 'sujet', lw=1.3)
arrow(ax, P(0, 0, 0), P(0, 0, 1.5), 'resultat', lw=1.3)
text(ax, 71, 26, r'$u_1$', 'sujet', 'm')
text(ax, 17, 26, r'$v_1$', 'sujet', 'm')
text(ax, 49, 40, r'$z_1$', 'resultat', 'm')
text(ax, 4, 9, r'plan $(u_1, v_1)$', 'sujet', 's', ha='left')
text(ax, 4, 5, r'$B$ = aire orientée', 'sujet', 's', ha='left')
text(ax, 60, 50, 'radical : orthogonal à tout', 'resultat', 's')
save(fig, '71-100')
