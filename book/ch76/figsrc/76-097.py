import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
M = [[2, 0, 1], [1, 3, 0], [0, 1, 4]]
pick = {0: 1, 1: 2, 2: 0}  # colonne -> ligne choisie
fig, ax = canvas(62)
for r in range(3):
    for c in range(3):
        on = pick[c] == r
        box(ax, 6 + 9 * c, 44 - 9 * r, 8, 8, 'sujet' if on else 'fixe', label=str(M[r][c]), weight='bold' if on else 'normal')
text(ax, 19, 20, r'lignes choisies : 2, 3, 1', 'sujet', 's')
box(ax, 40, 40, 44, 12, 'sujet', label=r'produit : $1\times1\times1$')
box(ax, 40, 24, 44, 12, 'varie', label=r'signe : 2 échanges, $+$')
box(ax, 40, 8, 44, 12, 'resultat', label=r'somme des $6$ rangements')
arrow(ax, (62, 40), (62, 36.5), 'fixe'); arrow(ax, (62, 24), (62, 20.5), 'fixe')
save(fig, '76-097')
