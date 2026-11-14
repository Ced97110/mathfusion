import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def table(x, y, rows, roles):
    for i, (v, r) in enumerate(zip(rows, roles)):
        box(ax, x, y - i * 8, 28, 8, r, label=v)
table(30, 66, ['(4, 6)', '(6, 4)'], ['sujet', 'sujet'])
text(ax, 44, 77, r'$\det=-20$', 'sujet', 'm')
table(3, 30, ['(4, 6)', '(10, 10)'], ['fixe', 'varie'])
table(57, 30, ['(8, 12)', '(6, 4)'], ['varie', 'fixe'])
arrow(ax, (36, 56), (17, 39), 'resultat', lw=1.3)
text(ax, 13, 47, 'ligne 1 + ligne 2', 'resultat', 's')
arrow(ax, (52, 56), (71, 39), 'limite', lw=1.3)
text(ax, 75, 47, 'ligne 1 + elle-même', 'limite', 's')
text(ax, 17, 12, r'$\det=-20$ : gardé', 'resultat', 's')
text(ax, 71, 12, r'$\det=-40$ : doublé', 'limite', 's')
save(fig, '59-064')
