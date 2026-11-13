import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 3, 63, r'corps à 5 éléments', 'encre', 's', ha='left')
xs = [3, 31, 59]; nums = ['4', '60', '2']; roles = ['fixe', 'sujet', 'fixe']
for x, n, r in zip(xs, nums, roles):
    box(ax, x, 36, 26, 22, r)
    text(ax, x + 13, 52, n, r, 'l', weight='bold')
text(ax, xs[0] + 13, 43, 'commutatif', 'fixe', 's')
text(ax, xs[2] + 13, 43, 'commutatif', 'fixe', 's')
text(ax, xs[1] + 13, 45, 'simple', 'sujet', 's')
text(ax, xs[1] + 13, 40, 'non commutatif', 'sujet', 's')
text(ax, 3, 17, r'corps à 3 éléments', 'encre', 's', ha='left')
box(ax, 33, 6, 26, 22, 'limite')
text(ax, 46, 22, '12', 'limite', 'l', weight='bold')
text(ax, 46, 12, 'pas simple', 'limite', 's')
save(fig, '73-210')
