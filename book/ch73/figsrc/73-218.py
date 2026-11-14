import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def grid(cx, cy, cols, rows, role):
    sp = 3.4
    for i in range(cols):
        for j in range(rows):
            disc(ax, cx + (i - (cols - 1) / 2) * sp, cy + (j - (rows - 1) / 2) * sp, 1.2, role)
text(ax, 21, 58, r'$|F|=3$', 'limite', 'l'); text(ax, 64, 58, r'$|F|=5$', 'resultat', 'l')
grid(21, 38, 4, 3, 'limite'); grid(64, 38, 10, 6, 'resultat')
text(ax, 21, 22, r'$A_4$ : 12 éléments', 'limite', 'm'); text(ax, 64, 22, r'$A_5$ : 60 éléments', 'resultat', 'm')
box(ax, 6, 6, 30, 9, 'limite', label='non simple', size='s')
box(ax, 49, 6, 30, 9, 'resultat', label='simple', size='s')
save(fig, '73-218')
