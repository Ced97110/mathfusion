import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(46)
u = 5
def plane(ox, vlen, role, label_v, label_a, arole):
    oy = 10
    poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + vlen * u), (ox, oy + vlen * u)], arole)
    arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.4)
    arrow(ax, (ox, oy), (ox, oy + vlen * u), 'varie', lw=1.4)
    text(ax, ox + u / 2, oy - 3, r'$u$', 'sujet', 'm')
    text(ax, ox, oy + vlen * u + 3, label_v, 'varie', 'm')
    text(ax, ox + u + 2, oy + vlen * u / 2, label_a, arole, 'm', ha='left')
plane(10, 3, 'sujet', r'$v$', 'aire 3', 'sujet')
plane(60, 1, 'resultat', r'$v/3$', 'aire 1', 'resultat')
arrow(ax, (32, 18), (50, 18), 'varie')
text(ax, 41, 22, 'diviser par 3', 'varie', 's')
save(fig, '71-101')
