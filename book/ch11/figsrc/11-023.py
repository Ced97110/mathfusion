import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 39, 57, 'États-Unis', 'autre', 's'); text(ax, 71, 57, 'métrique', 'sujet', 's')
rows = [('longueur', 'pied', 'mètre'), ('masse', 'livre', 'gramme'), ('capacité', 'gallon', 'litre')]
for r, (g, a, b) in enumerate(rows):
    y = 43 - r * 11
    text(ax, 3, y + 4, g, 'fixe', 's', ha='left')
    box(ax, 26, y, 26, 8, 'autre', label=a, size='s'); box(ax, 58, y, 26, 8, 'sujet', label=b, size='s')
text(ax, 3, 14, 'temps', 'fixe', 's', ha='left')
box(ax, 26, 10, 58, 8, 'resultat', label='20 minutes (les deux)', size='s')
save(fig, '11-023')
