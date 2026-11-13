import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# l'écriture, avec la partie entre parenthèses encadrée
box(ax, 20, 55, 26, 10, 'varie', label='(2 + 3)', size='l')
text(ax, 54, 60, '× 4', 'encre', 'l')
# droite A : avec l'étape 1
fA = numberline(ax, 6, 84, 38, 0, 20, step=1, labels=False, arrow_right=False)
text(ax, 6, 33.5, '0', 'fixe', 's')
for k in range(4):
    arrow(ax, (fA(5 * k), 38), (fA(5 * k + 5), 38), 'resultat', curve=-0.4)
text(ax, 44, 48, "avec l'étape 1 : 5 × 4 = 20", 'resultat', 's')
disc(ax, 84, 38, 1.2, 'resultat')
text(ax, 84, 33.5, '20', 'resultat', 's')
# droite B : sans l'étape 1
fB = numberline(ax, 6, 84, 14, 0, 20, step=1, labels=False, arrow_right=False)
text(ax, 6, 9.5, '0', 'fixe', 's')
for a, b in [(0, 2), (2, 6), (6, 10), (10, 14)]:
    arrow(ax, (fB(a), 14), (fB(b), 14), 'limite', curve=-0.4)
text(ax, 44, 24, "sans l'étape 1 : 2 + 12 = 14", 'limite', 's')
disc(ax, fB(14), 14, 1.2, 'limite')
text(ax, fB(14), 9.5, '14', 'limite', 's')
save(fig, '04-059')
