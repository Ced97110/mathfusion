import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rules = ['commutativité', 'associativité', 'distributivité', 'un zéro', 'des opposés']
for i, r in enumerate(rules):
    y = 54 - i * 11
    box(ax, 2, y, 34, 8, 'fixe', label=r, size='s')
    arrow(ax, (36, y + 4), (50, 31), 'sujet')
box(ax, 50, 22, 36, 18, 'sujet', label='anneau\ncommutatif', size='m')
text(ax, 68, 14, 'un seul mot', 'sujet', 's')
save(fig, '13-118')
