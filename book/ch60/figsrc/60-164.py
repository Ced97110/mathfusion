import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 45,r'$f=\lambda^2-1$ : $b_1=0$, $b_0=1$', 'sujet', 'm')
c = 11; x0 = 33; y0 = 15
cells = [['0', '1'], ['1', '0']]
roles = [['fixe', 'sujet'], ['resultat', 'resultat']]
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, roles[i][j], label=cells[i][j], size='l')
text(ax, x0 + 2 * c + 3, y0 + c + c / 2, r'$1$ voisin de', 'sujet', 's', ha='left')
text(ax, x0 + 2 * c + 3, y0 + c + c / 2 - 3.5, 'la diagonale', 'sujet', 's', ha='left')
text(ax, x0 - 3, y0 + c / 2 + 2, 'dernière ligne :', 'resultat', 's', ha='right')
text(ax, x0 - 3, y0 + c / 2 - 1.5, r'$b_0=1$, $b_1=0$', 'resultat', 's', ha='right')
text(ax, 44, 6, 'matrice de l’échange des coordonnées', 'encre', 's')
save(fig, '60-164')
