import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, 'Ligne de x = reste de x ÷ 3', 'encre', 'm')
box(ax, 3, 38, 14, 10, 'fixe', label='10', size='l'); box(ax, 3, 8, 14, 10, 'fixe', label='8', size='l')
for i, v in enumerate([1, 4, 7, 10]):
    box(ax, 38 + i * 12.5, 38, 12, 10, 'varie', label=str(v), size='m', lw=1.6 if v == 10 else 0.8)
for i, v in enumerate([2, 5, 8, 11]):
    box(ax, 38 + i * 12.5, 8, 12, 10, 'autre', label=str(v), size='m', lw=1.6 if v == 8 else 0.8)
arrow(ax, (18, 43), (37, 43), 'varie'); text(ax, 27.5, 47, 'reste 1', 'varie', 's')
arrow(ax, (18, 13), (37, 13), 'autre'); text(ax, 27.5, 17, 'reste 2', 'autre', 's')
text(ax, 62, 28, '3 valeurs : 0, 1, 2', 'resultat', 's')
save(fig, '47-016')
