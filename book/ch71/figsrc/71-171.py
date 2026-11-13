import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$P^{T}AP$', 'sujet', 'l')
text(ax, 44, 52, 'lignes de $P^T$ par colonnes de $AP$', 'encre', 's')
text(ax, 41, 45, 'colonne (8, 8)', 'fixe', 's'); text(ax, 69, 45, 'colonne (2, −2)', 'fixe', 's')
text(ax, 12, 30, 'ligne\n(1, 1)', 'fixe', 's'); text(ax, 12, 12, 'ligne\n(1, −1)', 'fixe', 's')
vals = [('8+8 = 16', 'resultat', 0, 0), ('2−2 = 0', 'fixe', 1, 0), ('8−8 = 0', 'fixe', 0, 1), ('2+2 = 4', 'resultat', 1, 1)]
for t, r, c, ro in vals:
    box(ax, 28 + c * 28, 24 - ro * 18 + 0, 26, 12, r, label=t, size='s')
text(ax, 44, 3, 'zéros hors de la diagonale', 'fixe', 's')
save(fig, '71-171')
