import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 4, 18, 55, 'sujet', label='(1 2 3)')
rows = [(50, [('(1 3)', 12), ('(1 2)', 12)], '2'),
        (36, [('(1 2)', 12), ('(2 3)', 12)], '2'),
        (22, [('(2 3)', 12), ('(1 3)', 12)], '2'),
        (8, [('(1 2)(1 2)', 24), ('(1 3)', 12), ('(1 2)', 12)], '4')]
for y, items, c in rows:
    x = 25
    for lab, w_ in items:
        box(ax, x, y, w_, 9, 'fixe' if w_ == 24 else 'varie', label=lab, size='s')
        x += w_ + 2
    text(ax, 84, y + 4.5, c, 'varie', 'l')
save(fig, '46-202')
