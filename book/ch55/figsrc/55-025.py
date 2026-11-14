import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
X = [14, 30, 46]; Y = [16, 32, 48]
for xi in X:
    for yi in Y:
        disc(ax, xi, yi, 0.5, 'fixe')
# diagonale sortie = entrée
line(ax, [(X[0] - 5, Y[0] - 5), (X[2] + 5, Y[2] + 5)], 'resultat', lw=1.2, dash=True)
for i in range(3):
    text(ax, X[i], 9, str(i), 'fixe', 's')
    text(ax, 7, Y[i], str(i), 'fixe', 's')
text(ax, 30, 3.5, 'entrée', 'fixe', 's')
text(ax, 7, 57, 'sortie', 'fixe', 's')
for i in range(3):
    disc(ax, X[i], Y[2], 2.4, 'fixe')
for i, v in enumerate((0, 1, 1)):
    disc(ax, X[i], Y[v], 2.4, 'autre')
for i in range(3):
    disc(ax, X[i], Y[i], 1.5, 'sujet')
text(ax, 58, 48, 'constante : 2, 2, 2', 'fixe', 's', ha='left')
text(ax, 58, 32, 'identité : 0, 1, 2', 'sujet', 's', ha='left', weight='bold')
text(ax, 58, 25, 'sortie = entrée', 'resultat', 's', ha='left')
text(ax, 58, 16, 'carré : 0, 1, 1', 'autre', 's', ha='left')
save(fig, '55-025')
