import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cls = [(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)]
for i, c in enumerate(cls):
    cx = 14 + i * 20
    r = 'sujet' if i == 0 else 'fixe'
    box(ax, cx - 8, 36, 16, 32, r, fill=True)
    for j in range(3): disc(ax, cx, 62 - j * 9, 2.2, r)
    text(ax, cx, 72, '{' + ', '.join(map(str, c)) + '}', r, 's')
    box(ax, cx - 5, 10, 10, 10, 'resultat', label=str(i), size='m')
    arrow(ax, (cx, 36), (cx, 20), 'varie', both=True, lw=1.2)
text(ax, 14, 38.8, 'noyau', 'sujet', 's', weight='bold')
text(ax, 24, 28, 'un à un', 'varie', 's')
text(ax, 44, 78, '12 éléments en 4 classes de 3', 'fixe', 's')
text(ax, 44, 4, 'même structure que l’image', 'resultat', 's', weight='bold')
save(fig, '52-160')
