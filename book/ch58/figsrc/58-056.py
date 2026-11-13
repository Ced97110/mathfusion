import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# A = [[2,1],[1,1]], B = [[1,-1],[-1,2]] : A B = I
A = [[2, 1], [1, 1]]; B = [[1, -1], [-1, 2]]
AB = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert AB == [[1, 0], [0, 1]]
# C = [[2,1],[1,3]] : det 5, inverse = (1/5) [[3,-1],[-1,2]]
C = [[2, 1], [1, 3]]; assert C[0][0] * C[1][1] - C[0][1] * C[1][0] == 5
def mat(x, y, m, role, w=18, size='m'):
    box(ax, x, y, w, 14, role, label='%s   %s\n%s   %s' % (m[0][0], m[0][1], m[1][0], m[1][1]), size=size)
# ligne du haut
text(ax, 44, 74, r'$\mathbb{Z}$ : l’inverse a des entiers', 'resultat', 's')
mat(3, 56, A, 'sujet')
text(ax, 24, 63, '×', 'encre', 'l')
mat(28, 56, [['1', '−1'], ['−1', '2']], 'sujet')
text(ax, 49, 63, '=', 'encre', 'l')
mat(54, 56, [['1', '0'], ['0', '1']], 'resultat')
text(ax, 44, 51, r'$\in GL_2(\mathbb{Z})$', 'resultat', 's')
# ligne du bas
text(ax, 44, 40, r'$\mathbb{Z}$ : l’inverse a des fractions', 'limite', 's')
mat(3, 20, C, 'sujet')
text(ax, 24, 27, '×', 'encre', 'l')
box(ax, 28, 20, 22, 14, 'limite', label='1/5 ×\n3   −1\n−1    2', size='s')
text(ax, 54, 27, '=', 'encre', 'l')
mat(58, 20, [['1', '0'], ['0', '1']], 'fixe')
text(ax, 44, 8, r'$\notin GL_2(\mathbb{Z})$', 'limite', 's')
save(fig, '58-056')
