import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def row(y, items, cnt):
    box(ax, 2, y, 19, 9, 'sujet', label='(1 2 3)')
    text(ax, 24, y + 4.5, '=', 'encre', 'm')
    for x, w_, lab, r in items:
        box(ax, x, y, w_, 9, r, label=lab, size='s' if w_ > 14 else 'm')
    return cnt
row(38, [(28, 12, '(1 3)', 'varie'), (42, 12, '(1 2)', 'varie')], 2)
text(ax, 41, 34, '2 échanges', 'varie', 's')
row(12, [(28, 12, '(1 2)', 'fixe'), (42, 12, '(1 2)', 'fixe'), (56, 12, '(1 3)', 'varie'), (70, 12, '(1 2)', 'varie')], 4)
brace(ax, 28, 54, 21, 'fixe', label='ne change rien', down=False)
text(ax, 54, 8, '4 échanges', 'varie', 's')
save(fig, '46-201')
