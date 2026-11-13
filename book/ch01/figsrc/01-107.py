import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, '1 carton vaut 10 paquets', 'fixe', 's')
text(ax, 44, 75, '10 paquets font 1 carton', 'sujet', 's')
text(ax, 25, 69, 'cartons', 'fixe', 's'); text(ax, 64, 69, 'paquets', 'fixe', 's')
box(ax, 10, 43, 30, 22, 'fixe', fill=False); text(ax, 25, 54, '0', 'fixe', 'm')
box(ax, 46, 43, 36, 22, 'fixe', fill=False)
for n in range(10):
    x = 49 + 2.5 * n
    poly(ax, [(x, 47), (x + 1.6, 47), (x + 1.6, 63), (x, 63)], 'fixe')
    for j in range(1, 10):
        line(ax, [(x, 47 + 1.6 * j), (x + 1.6, 47 + 1.6 * j)], 'fixe', lw=0.3)
text(ax, 78, 55, '10', 'encre', 'm')
arrow(ax, (60, 43), (30, 34.5), 'varie')
text(ax, 52, 38.5, 'échange', 'varie', 's', ha='left')
box(ax, 10, 12, 30, 22, 'fixe', fill=False)
poly(ax, [(14, 15), (30, 15), (30, 31), (14, 31)], 'resultat')
for j in range(1, 10):
    line(ax, [(14 + 1.6 * j, 15), (14 + 1.6 * j, 31)], 'resultat', lw=0.3)
    line(ax, [(14, 15 + 1.6 * j), (30, 15 + 1.6 * j)], 'resultat', lw=0.3)
text(ax, 36, 23, '1', 'encre', 'm')
box(ax, 46, 12, 36, 22, 'fixe', fill=False); text(ax, 64, 23, '0', 'fixe', 'm')
text(ax, 44, 6, 'même valeur : 100 boîtes', 'resultat', 's')
save(fig, '01-107')
