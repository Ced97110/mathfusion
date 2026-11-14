import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
c = 10
def grid(x0, y0, diag, role):
    for i in range(2):
        for j in range(2):
            on = (i == j)
            box(ax, x0 + j * c, y0 - i * c, c, c, role if on else 'fixe', label=diag if on else '0', size='l' if on else 'm')
    for s, xb in ((1, x0 - 1.5), (-1, x0 + 2 * c + 1.5)):
        line(ax, [(xb + s * 1.5, y0 + c + 1), (xb, y0 + c + 1), (xb, y0 - c + -1), (xb + s * 1.5, y0 - c - 1)], 'encre')
grid(6, 26, '1', 'sujet')
grid(52, 26, r'$\lambda$', 'varie')
arrow(ax, (30, 31), (48, 31), 'varie')
text(ax, 39, 36, r'$\times\,\lambda$', 'varie', 'm')
text(ax, 16, 9, r'$\mathbf{1}$ : identité $2\times2$', 'sujet', 's')
text(ax, 62, 9, r'$\lambda\mathbf{1}$ : $\lambda$ fois l’identité', 'varie', 's')
text(ax, 62, 44, r'$\lambda$ sur la diagonale', 'varie', 's')
text(ax, 16, 44, '1 sur la diagonale', 'sujet', 's')
save(fig, '60-153')
