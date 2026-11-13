import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('12', (2, 1, 0)), ('20', (2, 0, 1)), ('30', (1, 1, 1))]
text(ax, 55, 66, 'exposants de 2, 3, 5', 'fixe', 's')
for i, (n, ex) in enumerate(rows):
    y = 44 - i * 14
    text(ax, 12, y + 5, n, 'sujet', 'l', weight='bold')
    for j, e in enumerate(ex):
        box(ax, 26 + j * 20, y, 16, 10, 'sujet', label=str(e))
for j in range(3):
    box(ax, 24.5 + j * 20, 11, 19, 49, 'varie', fill=False, dash=True)
brace(ax, 24.5, 83.5, 9, 'varie', 'chaque colonne : une chaîne')
save(fig, '79-148')
