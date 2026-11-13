import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
assert 5 * 1 + 0 * 2 == 5 and 1 * 1 + 2 * 2 == 5
text(ax, 18, 70, 'liste de M', 'sujet', 's')
text(ax, 62, 70, 'écritures de (5, 4)', 'encre', 's')
rows = [
    (50, '(1, 0), (0, 1)', 'resultat', ['5·(1, 0) + 4·(0, 1)'], 'base : 1 écriture'),
    (30, '(1, 0)', 'limite', ['aucune écriture'], 'pas une base'),
    (6, '(1, 0), (2, 0), (0, 1)', 'limite', ['5·(1, 0)+0·(2, 0)+4·(0, 1)', '1·(1, 0)+2·(2, 0)+4·(0, 1)'], 'pas une base : 2 écritures'),
]
for y, lst, role, writs, verdict in rows:
    h = 15
    box(ax, 2, y, 32, h, 'sujet', label=lst, size='s')
    for i, wr in enumerate(writs):
        yy = y + h - 3 - i * 5.5 if len(writs) == 2 else y + h / 2 + 2
        text(ax, 38, yy, wr, role, 's', ha='left')
    text(ax, 38, y + 2.2, verdict, role, 's', ha='left', weight='bold')
save(fig, '58-046')
