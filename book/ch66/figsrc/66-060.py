import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 24, 63, 'tour de corps', 'sujet', 's')
box(ax, 4, 44, 36, 12, 'sujet', label='dimension 4')
box(ax, 4, 24, 36, 12, 'sujet', label='dimension 2')
box(ax, 4, 4, 36, 12, 'fixe', label=r'$\mathbb{Q}$')
for y in (24, 44):
    arrow(ax, (14, y - 8), (14, y), 'varie')
    text(ax, 24, y - 4, 'racine carrée', 'varie', 's', ha='left')
text(ax, 66, 63, 'groupe : 4 éléments', 'autre', 's')
box(ax, 46, 34, 40, 24, 'autre', fill=False)
for x in (53, 60, 72, 79):
    disc(ax, x, 46, 2.6, 'autre')
box(ax, 49, 40, 15, 12, 'varie', fill=False, dash=True)
box(ax, 68, 40, 15, 12, 'varie', fill=False, dash=True)
text(ax, 66, 28, 'deux étapes', 'varie', 's')
text(ax, 66, 22, 'de 2 éléments', 'varie', 's')
text(ax, 66, 10, 'une racine carrée par étape', 'resultat', 's')
save(fig, '66-060')
