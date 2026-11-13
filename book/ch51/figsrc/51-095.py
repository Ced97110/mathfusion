import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 28, 66, 32, 10, 'sujet', label='anneau', size='m')
cols = [(2, 'ab = ba', 'anneau\ncommutatif', 'resultat'),
        (32, 'inverse pour\nles non nuls', "un type\nd'anneau", 'resultat'),
        (62, 'inverse pour\ntout élément', '0 × x = 0,\njamais 1', 'limite')]
for x, cond, res, rrole in cols:
    cx = x + 12
    arrow(ax, (44, 65), (cx, 55), 'fixe')
    box(ax, x, 37, 24, 17, 'varie', label=cond, size='s')
    arrow(ax, (cx, 36), (cx, 27), 'varie')
    box(ax, x, 6, 24, 20, rrole, label=res, size='s')
save(fig, '51-095')
