import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# 16 points in a 4 x 4 grid = the 16 elements of the field
x0, y0, d = 34, 14, 6.5
for i in range(4):
    for j in range(4):
        disc(ax, x0 + i * d, y0 + j * d, 2.0, 'sujet')
text(ax, x0 + 1.5 * d, 6, '16 éléments', 'sujet', 's')
box(ax, 2, 40, 22, 12, 'sujet', label=r'$GF(2^4)$')
text(ax, 13, 56, 'logiciel', 'fixe', 's')
box(ax, 64, 40, 22, 12, 'autre', label=r'$\mathbb{F}_{2^4}$', size='l')
text(ax, 75, 56, 'ce chapitre', 'fixe', 's')
arrow(ax, (20, 40), (x0 - 2, y0 + 3 * d + 1), 'fixe')
arrow(ax, (68, 40), (x0 + 3 * d + 2, y0 + 3 * d + 1), 'fixe')
save(fig, '67-062')
