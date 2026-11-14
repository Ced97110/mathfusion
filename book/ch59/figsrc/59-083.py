import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['2', '0'], ['0', '10']], [['sujet', 'fixe'], ['fixe', 'autre']], 44, 24)
box(ax, 54.5, 23.5, 11, 11, 'varie', fill=False, dash=True, lw=1.0)
box(ax, 3, 36, 32, 10, 'sujet', label=r'$d_1=2$')
arrow(ax, (35.5, 41), (43.5, 41), 'sujet')
box(ax, 70, 24, 16, 10, 'autre', label=r'$d_2=10$', size='s')
arrow(ax, (70, 29), (66.5, 29), 'autre')
text(ax, 60, 17, 'sous-matrice', 'varie', 's')
text(ax, 44, 8, 'ligne et colonne 1 retirées', 'fixe', 's')
save(fig, '59-083')
