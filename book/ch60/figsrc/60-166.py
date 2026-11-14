import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'doublement du plan : deux blocs', 'encre', 's')
c = 13; x0 = 31; y0 = 14
for i in range(2):
    for j in range(2):
        on = i == j
        box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, 'sujet' if on else 'fixe', label='2' if on else '0', size='l' if on else 'm')
text(ax, x0 - 3, y0 + c + c / 2, r'bloc $B_1=(2)$', 'sujet', 's', ha='right')
text(ax, x0 + 2 * c + 3, y0 + c / 2, r'bloc $B_2=(2)$', 'sujet', 's', ha='left')
text(ax, x0 + 2 * c + 3, y0 + c + c / 2, '0 hors des blocs', 'fixe', 's', ha='left')
text(ax, 44, 5, r'$B_i$ = compagnon de $\lambda-2$', 'encre', 's')
save(fig, '60-166')
