import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'x² + 6x', 'sujet', 'l')
rows = [('le nombre devant x', '6'), ('sa moitié', '3'), ('le carré de la moitié', '9'), ('le carré complet', '(x + 3)²')]
for i, (a, v) in enumerate(rows):
    y = 58 - i * 16
    box(ax, 3, y, 46, 10, 'fixe', label=a, size='s')
    box(ax, 54, y, 30, 10, 'resultat' if i == 3 else 'sujet', label=v)
    if i < 3: arrow(ax, (69, y - 0.5), (69, y - 5.5), 'varie')
save(fig, '23-046')
