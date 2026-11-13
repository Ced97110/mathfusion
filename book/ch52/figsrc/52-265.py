import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
c = 7; x0 = 14; y0 = 12
for i in range(4):
    for j in range(6):
        ok = (i % 2 == j % 2)
        box(ax, x0 + i * c, y0 + j * c, c, c, 'resultat' if ok else 'limite', lw=0.5, r=0.4)
for i in range(4): text(ax, x0 + i * c + c / 2, y0 - 2.5, str(i), 'fixe', 's')
for j in range(6): text(ax, x0 - 3, y0 + j * c + c / 2, str(j), 'fixe', 's')
text(ax, x0 + 2 * c, 5, 'reste par 4', 'encre', 's')
text(ax, 3, y0 + 3 * c, 'reste par 6', 'encre', 's', rot=90)
box(ax, 50, 46, 6, 6, 'resultat', lw=0.5, r=0.4); text(ax, 59, 49, 'atteintes : 12', 'resultat', 's', ha='left')
box(ax, 50, 36, 6, 6, 'limite', lw=0.5, r=0.4); text(ax, 59, 39, 'non atteintes : 12', 'limite', 's', ha='left')
save(fig, '52-265')
