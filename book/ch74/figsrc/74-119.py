import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, y0, cw, ch = 6, 14, 14, 12
M = [[2, 5], [7, 4]]
for i in range(2):
    for j in range(2):
        d = i == j
        box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, 'sujet' if d else 'fixe', label=str(M[i][j]), size='l', weight='bold' if d else 'normal')
line(ax, [(x0 + 3, y0 + 2 * ch - 3), (x0 + 2 * cw - 3, y0 + 3)], 'varie', lw=1.2, dash=True)
text(ax, x0 + cw, 46, 'diagonale : 2 et 4', 'sujet', 's')
text(ax, x0 + cw, 8, '5 et 7 : ignorés', 'fixe', 's')
arrow(ax, (x0 + 2 * cw + 3, y0 + ch), (48, y0 + ch), 'varie', lw=1.1)
box(ax, 50, y0 + ch - 6, 36, 12, 'resultat', label='tr = 2 + 4 = 6', size='m')
save(fig, '74-119')
