import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(64)
ox, oy, u = 22, 36, 9
line(ax, [(8, oy), (38, oy)], 'fixe'); line(ax, [(ox, 20), (ox, 54)], 'fixe')
text(ax, 40.5, oy, r'$x$', 'fixe', 's'); text(ax, ox, 57, r'$y$', 'fixe', 's')
disc(ax, ox + u, oy + u, 1.3, 'sujet'); disc(ax, ox + u, oy - u, 1.3, 'sujet')
text(ax, ox + u, oy + u + 3.5, '(1, 1)', 'sujet', 's')
text(ax, ox + u, oy - u - 3.5, r'$(1,-1)$', 'sujet', 's')
arrow(ax, (ox + u + 3, oy + u), (50, oy + u), 'varie')
arrow(ax, (ox + u + 3, oy - u), (50, oy - u), 'varie')
box(ax, 51, oy + u - 4, 30, 8, 'resultat', label=r'$Q=16$')
box(ax, 51, oy - u - 4, 30, 8, 'resultat', label=r'$Q=4$')
for k, (x, t) in enumerate(((5, r'$5x^2$'), (34, r'$6xy$'), (63, r'$5y^2$'))):
    box(ax, x, 3, 20, 8, 'sujet', label=t)
text(ax, 29.5, 7, '+', 'sujet', 'l'); text(ax, 58.5, 7, '+', 'sujet', 'l')
text(ax, 44, 15, 'deux coordonnées par terme', 'sujet', 's')
save(fig, '71-111')
