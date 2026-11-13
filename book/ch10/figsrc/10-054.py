import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = (16, 44, 72); roles = ('sujet', 'varie', 'autre'); caps = ('n : facteur', 'a : terme 1', 'b : terme 2')
for c, r, t in zip(cols, roles, caps):
    box(ax, c - 12, 50, 24, 10, r, label=t, size='s')
text(ax, 30, 55, r'$\times$', 'encre', 'l'); text(ax, 58, 55, '+', 'encre', 'l')
rows = ((3, 2, 5), (7, 20, 3), (25, 20, 3))
for k, row in enumerate(rows):
    y = 38 - k * 12
    for c, r, v in zip(cols, roles, row):
        text(ax, c, y, str(v), r, 'l', weight='bold')
for c in cols: line(ax, [(c, 46), (c, 8)], 'fixe', lw=0.5, dash=True)
save(fig, '10-054')
