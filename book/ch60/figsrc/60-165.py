import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$\lambda^2-2\lambda+1=\lambda^2-b_1\lambda-b_0$', 'sujet', 's')
text(ax, 44, 40, r'$b_1=2$ et $b_0=-1$', 'sujet', 's')
c = 11; x0 = 33; y0 = 15
cells = [['0', '1'], ['−1', '2']]
roles = [['fixe', 'sujet'], ['resultat', 'resultat']]
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, roles[i][j], label=cells[i][j], size='l')
text(ax, x0 + 2 * c + 3, y0 + c + c / 2, '1 au-dessus', 'sujet', 's', ha='left')
text(ax, x0 + 2 * c + 3, y0 + c + c / 2 - 3.5, 'de la diagonale', 'sujet', 's', ha='left')
text(ax, x0 - 3, y0 + c / 2 + 2, 'dernière ligne :', 'resultat', 's', ha='right')
text(ax, x0 - 3, y0 + c / 2 - 1.5, r'$b_0=-1$, $b_1=2$', 'resultat', 's', ha='right')
text(ax, 44, 6, 'degré 2 : quatre cases', 'encre', 's')
save(fig, '60-165')
