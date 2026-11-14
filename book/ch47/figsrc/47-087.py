import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, '6 permutations de 3 objets', 'fixe', 's')
for k in range(3):
    x = 5 + k * 27.5
    box(ax, x, 46, 25, 9, 'sujet', label='2 éléments', size='s')
    box(ax, x, 12, 25, 9, 'autre', label='2 éléments', size='s')
    arrow(ax, (x + 12.5, 45.5), (x + 12.5, 21.5), 'varie', both=True)
text(ax, 44, 59.5, '3 classes à gauche', 'sujet', 'm')
text(ax, 44, 6, '3 classes à droite', 'autre', 'm')
text(ax, 44, 33.5, 'inverse : un pour un', 'varie', 's')
save(fig, '47-087')
