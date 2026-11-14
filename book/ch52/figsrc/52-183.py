import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 20, 58, 'on la dessine', 'sujet', 's')
text(ax, 66, 58, 'on ne la dessine pas', 'fixe', 's')
for a in range(4):
    for b in range(5):
        box(ax, 5 + b * 6, 28 + a * 6, 6, 6, 'sujet', r=0.3)
gx, gy, n, s = 50, 24, 16, 2
for i in range(n + 1):
    line(ax, [(gx + i * s, gy), (gx + i * s, gy + n * s)], 'fixe', lw=0.3)
    line(ax, [(gx, gy + i * s), (gx + n * s, gy + i * s)], 'fixe', lw=0.3)
text(ax, gx + n * s / 2, gy + n * s / 2, '9 215', 'fixe', 'l', weight='bold')
text(ax, 20, 18, '4 × 5 = 20 cases', 'sujet', 's')
text(ax, 66, 18, '95 × 97 = 9 215 cases', 'fixe', 's')
text(ax, 44, 10, 'La grille dit : une solution existe.', 'resultat', 's')
text(ax, 44, 4.5, 'Elle ne dit pas où elle est.', 'varie', 's')
save(fig, '52-183')
