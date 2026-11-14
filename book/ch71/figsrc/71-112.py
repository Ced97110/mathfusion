import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(60)
text(ax, 44, 55, 'tous les termes de degré 2', 'resultat', 's')
for x, t, g in ((5, r'$5x^2$', 'degré 2'), (33, r'$6xy$', 'degré 1 + 1 = 2'), (61, r'$5y^2$', 'degré 2')):
    box(ax, x, 40, 22, 8, 'sujet', label=t)
    text(ax, x + 11, 36, g, 'resultat', 's')
text(ax, 28, 44, '+', 'sujet', 'l'); text(ax, 56, 44, '+', 'sujet', 'l')
text(ax, 44, 29, 'degré 1 : pas homogène', 'limite', 's')
box(ax, 5, 16, 22, 8, 'sujet', label=r'$x^2$')
box(ax, 33, 16, 22, 8, 'limite', label=r'$x$')
text(ax, 30, 20, '+', 'sujet', 'l')
text(ax, 16, 12, 'degré 2', 'resultat', 's')
text(ax, 44, 12, 'degré 1', 'limite', 's')
save(fig, '71-112')
