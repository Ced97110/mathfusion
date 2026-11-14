import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 9; x0 = 31; y0 = 8
M = [['1', '0', '0'], ['0', '0', '1'], ['0', '−1', '2']]
for i in range(3):
    for j in range(3):
        role = 'sujet' if (i, j) == (0, 0) else ('varie' if i > 0 and j > 0 else 'fixe')
        box(ax, x0 + j * c, y0 + (2 - i) * c, c, c, role, label=M[i][j], size='l')
text(ax, 44, 44, 'forme rationnelle', 'encre', 'm', weight='bold')
text(ax, 14, y0 + 2.5 * c, 'bloc 1 × 1\n' + r'$\lambda-1$', 'sujet', 's')
arrow(ax, (25, y0 + 2.5 * c), (x0 - 0.5, y0 + 2.5 * c), 'sujet')
text(ax, 73, y0 + c, 'bloc 2 × 2\n' + r'$(\lambda-1)^2$', 'varie', 's')
arrow(ax, (63, y0 + c), (x0 + 3 * c + 0.5, y0 + c), 'varie')
save(fig, '60-213')
