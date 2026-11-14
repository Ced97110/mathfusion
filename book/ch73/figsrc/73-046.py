import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
c = 9
def grid(x, y, v, diag_role, other):
    for i in range(2):
        for j in range(2):
            role = diag_role if i == j else other[(i, j)]
            box(ax, x+j*c, y+(1-i)*c, c, c, role, label=v[i][j], size='l')
grid(10, 12, [['1', '5'], ['0', '1']], 'sujet', {(0, 1): 'varie', (1, 0): 'fixe'})
grid(58, 12, [['2', '0'], ['0', '1']], 'limite', {(0, 1): 'fixe', (1, 0): 'fixe'})
text(ax, 19, 36, r'$i \neq j$ : triangulaire', 'sujet', 's'); text(ax, 67, 36, r'$i = j$ : pas de $b$ hors diag.', 'limite', 's')
text(ax, 19, 6, r'diagonale : $1 \times 1 = 1$', 'resultat', 's'); text(ax, 67, 6, r'diagonale : $2 \times 1 = 2$', 'limite', 's')
save(fig, '73-046')
