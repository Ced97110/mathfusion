import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    """Grid of square cells; vals[i][j] text, roles[i][j] role (None = empty cell)."""
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(62)
top = 54; xs = (8, 36, 64)
for k, n in enumerate((3, 2, 1)):
    for b in range(n):
        yb = top - 2.6 - b * 3.4
        box(ax, xs[k], yb, 18, 2.6, 'varie' if (k == 0 and b == 0) else 'sujet', r=0.3, lw=0.6)
for k in range(2):
    arrow(ax, (xs[k] + 19.5, top - 5), (xs[k + 1] - 1.5, top - 5), 'fixe')
text(ax, 4, 58, 'élimination de Gauss', 'sujet', 's', ha='left')
text(ax, 17, 41, '3 équations', 'sujet', 's')
text(ax, 45, 41, '2 équations', 'sujet', 's')
bot = 11
for k, s in enumerate((16, 11, 6)):
    box(ax, xs[k], bot, s, s, 'autre', r=0.3, lw=0.6)
box(ax, xs[0], bot, 5, 5, 'varie', r=0.3, lw=0.6)
for k in range(2):
    arrow(ax, (xs[k] + (16, 11)[k] + 1.5, bot + 6), (xs[k + 1] - 1.5, bot + 6), 'fixe')
text(ax, 4, 33, 'base symplectique', 'autre', 's', ha='left')
text(ax, 17, 6, 'partie traitée', 'varie', 's')
text(ax, 62, 6, 'puis on recommence', 'fixe', 's')
save(fig, '71-103')
