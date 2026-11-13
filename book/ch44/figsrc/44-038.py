import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [40, 52, 64, 76]; R = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 3, 2]]; ys = [58, 36, 14]
roles = ['sujet', 'fixe', 'resultat']
text(ax, 2, 36, r'après $s$', 'varie', 's', ha='left'); text(ax, 2, 14, r'après $r$ : $r \circ s$', 'autre', 's', ha='left')
for row, y, ro in zip(R, ys, roles):
    for x, v in zip(xs, row): disc(ax, x, y, 4.2, ro, label=str(v))
for i, ro in enumerate(['varie', 'autre']):
    for x in xs: arrow(ax, (x, ys[i] - 4.7), (x, ys[i + 1] + 4.7), ro)
save(fig, '44-038')
