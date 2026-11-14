import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 11; x0 = 27; y0 = 6
M = [['1', '0', '0'], ['0', '1', '1'], ['0', '0', '1']]
for i in range(3):
    for j in range(3):
        role = 'sujet' if (i, j) == (0, 0) else ('varie' if i > 0 and j > 0 else 'fixe')
        box(ax, x0 + j * c, y0 + (2 - i) * c, c, c, role, label=M[i][j], size='l')
text(ax, 11, y0 + 2.5 * c, r'$J_1$', 'sujet', 'l', weight='bold')
arrow(ax, (17, y0 + 2.5 * c), (x0 - 0.5, y0 + 2.5 * c), 'sujet')
text(ax, 11, y0 + c, r'$J_2$', 'varie', 'l', weight='bold')
arrow(ax, (17, y0 + c), (x0 - 0.5, y0 + c), 'varie')
text(ax, 75, y0 + 2.5 * c, 'taille 1', 'sujet', 's')
text(ax, 75, y0 + c, 'taille 2', 'varie', 's')
arrow(ax, (68, y0 + 2.5 * c), (x0 + 3 * c + 0.5, y0 + 2.5 * c), 'sujet')
arrow(ax, (68, y0 + c), (x0 + 3 * c + 0.5, y0 + c), 'varie')
save(fig, '60-215')
