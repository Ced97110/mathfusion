import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 61, r'$\circ$', 'encre', 'xl')
text(ax, 44, 52, 'même signe, deux sens', 'fixe', 's')
box(ax, 2, 6, 40, 40, 'autre'); box(ax, 46, 6, 40, 40, 'sujet')
text(ax, 22, 40, 'chapitre 42', 'autre', 'm', weight='bold'); text(ax, 66, 40, 'chapitre 78', 'sujet', 'm', weight='bold')
text(ax, 22, 34, 'composition', 'autre', 's'); text(ax, 66, 34, 'produit de Jordan', 'sujet', 's')
for i, (n, x) in enumerate([('3', 8), ('6', 22), ('7', 36)]):
    disc(ax, x, 20, 3.5, 'autre', label=n)
    if i: arrow(ax, (x - 14 + 3.8, 20), (x - 3.8, 20), 'varie'); text(ax, x - 7, 25, [r'$\times 2$', r'$+1$'][i - 1], 'varie', 's')
box(ax, 49, 20, 34, 8, 'sujet', label=r'$a,\,b$ : matrices', size='s', fill=False)
arrow(ax, (66, 20), (66, 14.5), 'varie')
box(ax, 49, 7, 34, 8, 'sujet', label=r'$(ab+ba)/2$', size='s')
save(fig, '78-062')
