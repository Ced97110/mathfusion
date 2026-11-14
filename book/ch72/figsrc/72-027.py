import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [('symétrie', '(1, 2), (3, 4) : 11', '(3, 4), (1, 2) : 11'),
        ('additivité', '(1, 2) + (1, 0) = (2, 2)', '(2, 2), (3, 4) : 14 = 11 + 3'),
        ('homogénéité', '2 × (1, 2) = (2, 4)', '(2, 4), (3, 4) : 22 = 2 × 11')]
for i, (n, a, b) in enumerate(rows):
    y = 56 - i*26
    box(ax, 2, y, 26, 20, 'sujet', label=n, size='s')
    box(ax, 32, y, 54, 20, 'resultat' if i else 'resultat', fill=True)
    text(ax, 59, y + 14, a, 'encre', 's'); text(ax, 59, y + 6, b, 'resultat', 's')
save(fig, '72-027')
