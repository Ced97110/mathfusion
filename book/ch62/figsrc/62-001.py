import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [(34, 'fractions\n$x^2-2$ sans racine', '$\\sqrt{2}$\nson carré vaut 2'),
        (8, 'réels\n$x^2+1$ sans racine', '$i$\nson carré vaut −1')]
for y, left, right in rows:
    box(ax, 2, y, 31, 14, 'fixe', label=left, size='s')
    box(ax, 55, y, 31, 14, 'resultat', label=right, size='s')
    arrow(ax, (34.5, y + 7), (53.5, y + 7), 'varie', lw=1.2)
    text(ax, 44, y + 11, 'on ajoute', 'varie', 's')
text(ax, 44, 28.5, 'le même geste, deux fois', 'encre', 'm')
text(ax, 44, 54, 'pas de racine : on fabrique le nombre', 'encre', 'm')
save(fig, '62-001')
