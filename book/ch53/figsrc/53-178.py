import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, 'chaque pas de RSA : un chapitre', 'encre', 'm', weight='bold')
rows = [('Euclide (chap. 5)', 'trouver la clé privée'),
        ('base 2 (chap. 1)', 'calculer vite'),
        ('Lagrange (chap. 47)', 'prouver que ça marche')]
for i, (a, b) in enumerate(rows):
    y = 52 - i * 20
    box(ax, 3, y, 34, 12, 'autre', label=a, size='s')
    arrow(ax, (37, y + 6), (49, y + 6), 'varie')
    box(ax, 49, y, 36, 12, 'sujet', label=b, size='s')
save(fig, '53-178')
