import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$\bar{3}+\bar{2}=\bar{1}$', 'sujet', 'xl')
for x, s in ((14, 'choisir'), (44, 'additionner'), (74, 'reprendre la classe')):
    text(ax, x, 57, s, 'varie', 's')
rows = (('3 et 2', '3 + 2 = 5', 'reste 1'), ('7 et 6', '7 + 6 = 13', 'reste 1'))
for k, (a, b, c) in enumerate(rows):
    y = 40 - k * 16
    box(ax, 3, y - 5, 22, 10, 'varie', label=a)
    box(ax, 31, y - 5, 26, 10, 'fixe', label=b)
    arrow(ax, (25.5, y), (30.5, y), 'varie'); arrow(ax, (57.5, y), (63, y + (6 if k == 0 else -6) * 0.0), 'varie')
box(ax, 63, 14, 22, 36, 'resultat', label=None)
text(ax, 74, 38, r'$\bar{1}$', 'resultat', 'xl')
text(ax, 74, 28, 'classe de 1', 'resultat', 's')
text(ax, 74, 20, 'les deux fois', 'resultat', 's')
save(fig, '52-069')
