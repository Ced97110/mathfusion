import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
yb = 18
items = [(8, r'$-$', 8, 'autre'), (19, '15', 12, 'sujet'), (31, r'$-$', 8, 'varie'), (47, r'$-$', 8, 'autre'), (57, '6', 10, 'sujet')]
for c, t, wd, r in items:
    box(ax, c - wd / 2, yb, wd, 10, r, label=t, size='l')
text(ax, 40, yb + 5, '(', 'fixe', 'xl'); text(ax, 66, yb + 5, ')', 'fixe', 'xl')
for c, t, r in ((8, 'négatif', 'autre'), (31, 'moins', 'varie'), (47, 'négatif', 'autre')):
    text(ax, c, yb - 4, t, r, 's')
text(ax, 44, 36, 'négatif 15 moins négatif 6', 'encre', 'm')
save(fig, '13-029')
