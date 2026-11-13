import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 44, 6, 42, 58, 'sujet')
text(ax, 65, 58, 'anneau', 'sujet', 'xl', weight='bold')
for i, s in enumerate(['addition  +', 'multiplication  ×', 'courte liste de règles']):
    box(ax, 47, 38 - 15 * i, 36, 11, 'fixe', label=s, size='s')
for i, nom in enumerate(['entiers', 'polynômes', 'heures', 'matrices']):
    y = 52 - 14 * i
    box(ax, 2, y, 26, 11, 'fixe', label=nom, size='s')
    arrow(ax, (28, y + 5.5), (44, y + 5.5), 'varie')
save(fig, '51-006')
