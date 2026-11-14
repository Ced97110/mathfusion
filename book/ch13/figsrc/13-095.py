import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, n, p, q, k in ((50, 7, 10, 12, '3 + 12 = 5 + 10'), (22, 1, 4, 6, '3 + 6 = 5 + 4')):
    box(ax, 3, y, 22, 9, 'sujet', label='(3, 5)')
    arrow(ax, (27, y + 4.5), (47, y + 4.5), 'varie')
    text(ax, 37, y + 10, f'+ {n} aux deux', 'varie', 's')
    box(ax, 50, y, 26, 9, 'autre', label=f'({p}, {q})')
    text(ax, 50, y - 5, k, 'resultat', 'm', ha='left')
save(fig, '13-095')
