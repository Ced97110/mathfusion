import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 4, 46, 80, 20, 'resultat', fill=False, dash=True)
text(ax, 44, 62, 'un nouvel ensemble : 4 éléments', 'resultat', 'm')
for i in range(4):
    x = 10 + i * 20
    box(ax, x - 7, 49, 14, 8, 'sujet', label=r'$\bar{%d}$' % i, size='m')
arrow(ax, (64, 48), (64, 33), 'varie')
text(ax, 44, 40, 'ouvrir', 'varie', 's', ha='right')
box(ax, 6, 6, 76, 26, 'sujet', label=None)
text(ax, 44, 26, r'$\bar{3}$ = …, −1, 3, 7, 11, …', 'sujet', 'm')
text(ax, 44, 19, 'un élément = une collection', 'sujet', 's')
text(ax, 44, 12.5, 'infinie d’entiers', 'sujet', 's')
save(fig, '52-068')
