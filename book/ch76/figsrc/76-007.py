import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
heads = ['café', 'croissant', 'total (€)']
for j, h in enumerate(heads): text(ax, 15 + j * 15, 58, h, 'fixe', 's')
data = [[1, 1, 5], [2, 1, 8]]
for i, row in enumerate(data):
    for j, v in enumerate(row):
        box(ax, 8 + j * 15, 38 - i * 12 + 1, 14, 10, 'sujet', label=str(v), size='l')
text(ax, 3, 44, '', 'fixe', 's')
arrow(ax, (54, 40), (62, 40), 'varie', lw=1.4)
text(ax, 58, 46, 'direct', 'varie', 's')
box(ax, 64, 33, 20, 14, 'resultat', label=r'$x=3$', size='l')
text(ax, 74, 29, 'prix du café', 'resultat', 's')
text(ax, 30, 10, 'six nombres, sans étape', 'varie', 's')
save(fig, '76-007')
