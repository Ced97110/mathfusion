import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 17, 59, 'nombre', 'encre', 's')
text(ax, 65, 59, 'son carré', 'encre', 's')
rows = [(43, 'positif', 'positif', 'fixe'), (28, 'négatif', 'positif', 'fixe'), (13, r'$i$', r'$-1$ : négatif', 'sujet')]
for y, a, b, role in rows:
    box(ax, 4, y, 26, 11, role, label=a, size='m')
    arrow(ax, (31, y + 5.5), (47, y + 5.5), 'varie')
    box(ax, 48, y, 36, 11, role, label=b, size='m')
text(ax, 44, 4.5, r'$i$ : ni positif ni négatif', 'sujet', 's')
save(fig, '39-044')
