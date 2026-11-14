import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
assert 3 * 2 * 2 * 2 * 2 == 48
xs = [5 + 16.5 * i for i in range(5)]
y = 28
text(ax, 44, 54, '48 = 3 × 2 × 2 × 2 × 2', 'encre', 'l')
for i, x in enumerate(xs):
    box(ax, x, y, 12, 12, 'sujet' if i == 0 else 'autre', label='3' if i == 0 else '2', size='l')
    if i < 4:
        text(ax, x + 14.25, y + 6, '×', 'fixe', 'm')
brace(ax, xs[0], xs[0] + 12, y - 1, 'sujet', label='chaîne 1')
brace(ax, xs[1], xs[4] + 12, y - 1, 'autre', label='chaîne 2 : 16, 8, 4, 2')
save(fig, '56-100')
