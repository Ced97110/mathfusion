import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 48, r'$P_{ij}$ : son propre inverse', 'encre', 'm')
tabs = [(3, [('(4, 6)', 'sujet'), ('(6, 4)', 'autre')], 'départ'),
        (34, [('(6, 4)', 'autre'), ('(4, 6)', 'sujet')], '1 échange'),
        (65, [('(4, 6)', 'sujet'), ('(6, 4)', 'autre')], '2 échanges')]
for x, rows, name in tabs:
    for i, (v, role) in enumerate(rows):
        box(ax, x, 26 - i * 9, 20, 9, role, label=v)
    text(ax, x + 10, 14, name, 'encre', 's')
for x in (24.5, 55.5):
    arrow(ax, (x, 26), (x + 8, 26), 'varie', lw=1.2, both=False)
    text(ax, x + 4, 31, r'$P_{12}$', 'varie', 's')
save(fig, '59-057')
