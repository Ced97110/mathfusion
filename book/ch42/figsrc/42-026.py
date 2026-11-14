import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 4, 14, 24, 30, 'sujet')
text(ax, 16, 34, r'$S$', 'sujet', 28); text(ax, 16, 20, 'un ensemble', 'sujet', 's')
for y, t in zip([44, 29, 14], ['objets de la table', 'nombres de 1 à 10', 'élèves d’une classe']):
    arrow(ax, (28.5, 29), (47.5, y), 'fixe')
    box(ax, 48, y - 5, 38, 10, 'fixe', label=t, size='s')
save(fig, '42-026')
