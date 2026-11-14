import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 34, 6, 20, 50, 'sujet', label=r'$Q$', size='l')
text(ax, 44, 59, 'la règle', 'sujet', 's')
for y, a, b in [(40, '(3, 4)', '25'), (16, '(1, 2)', '5')]:
    box(ax, 4, y - 5, 20, 10, 'fixe', label=a)
    arrow(ax, (25, y), (33, y), 'varie')
    arrow(ax, (55, y), (63, y), 'varie')
    box(ax, 64, y - 5, 20, 10, 'resultat', label=b)
text(ax, 14, 50, 'un vecteur', 'fixe', 's')
text(ax, 74, 50, 'un nombre', 'resultat', 's')
save(fig, '73-129')
