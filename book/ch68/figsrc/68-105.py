import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = [30 + 9 * i for i in range(5)]
rows = [(52, r'$x$', [0, 0, 1, 1, 1], 'sujet'), (38, r'$y$', [1, 1, 1, 0, 0], 'autre'), (20, r'$x+y$', [1, 1, 0, 1, 1], 'resultat')]
text(ax, 44, 62, 'plein = 1, vide = 0', 'fixe', 's')
for y, lab, bits, role in rows:
    text(ax, 4, y, lab, role, 'm', ha='left')
    for x, b in zip(X, bits):
        disc(ax, x, y, 3, role, fill=bool(b))
for i in range(5):
    if rows[0][2][i] != rows[1][2][i]:
        arrow(ax, (X[i], 34), (X[i], 25), 'varie')
line(ax, [(74, 52), (74, 38)], 'varie')
text(ax, 80, 45, 'distance', 'varie', 's')
text(ax, 80, 41, '4', 'varie', 's')
text(ax, 80, 20, 'poids 4', 'resultat', 's')
text(ax, 44, 8, 'la somme est un mot non nul du code', 'resultat', 's')
save(fig, '68-105')
