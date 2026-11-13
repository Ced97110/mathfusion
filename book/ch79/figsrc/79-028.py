import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def row(y, items, role, dash=False):
    for i, s in enumerate(items): box(ax, 3 + 17 * i, y, 14, 8, role, label=s, size='s', dash=dash)
text(ax, 3, 57, '4 couples : même nombre', 'varie', 's', ha='left')
row(46, ['(1, 1)', '(2, 2)', '(3, 3)', '(6, 6)'], 'varie')
text(ax, 3, 39, '5 couples : nombres différents', 'sujet', 's', ha='left')
row(28, ['(1, 2)', '(1, 3)', '(1, 6)', '(2, 6)', '(3, 6)'], 'sujet')
text(ax, 3, 20, 'absents : 2 et 3 sans lien', 'limite', 's', ha='left')
row(8, ['(2, 3)', '(3, 2)'], 'limite', dash=True)
save(fig, '79-028')
