import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$G$ : 6 permutations', 'fixe', 's')
box(ax, 10, 28, 44, 30, 'varie', fill=False, dash=True)
for i, x in enumerate((22, 44, 66)):
    for y in (48, 36):
        disc(ax, x, y, 4.2, 'fixe' if i == 2 else 'varie')
text(ax, 32, 22, r'$HN$ : 4 éléments', 'varie', 's')
text(ax, 66, 22, 'hors de $HN$', 'fixe', 's')
text(ax, 44, 12, '4 ne divise pas 6', 'limite', 'm')
text(ax, 44, 5, r'$HN$ n’est pas un sous-groupe', 'limite', 's')
save(fig, '48-111')
