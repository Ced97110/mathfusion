import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'un carré = un sous-groupe', 'fixe', 's')
rows = [('1 élément', 1), ('2 éléments', 3), ('4 éléments', 1)]
for i, (lab, n) in enumerate(rows):
    c = 46 - 14 * i
    text(ax, 2, c, lab, 'encre', 'm', ha='left')
    for k in range(n):
        box(ax, 34 + 13 * k, c - 4.5, 10, 9, 'sujet')
    text(ax, 84, c, f'= {n}', 'encre', 'm', ha='right')
text(ax, 44, 5, 'total : 1 + 3 + 1 = 5', 'resultat', 'l')
save(fig, '63-009')
