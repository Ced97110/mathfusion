import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
text(ax, 44, 62, 'étape 5 : on retranche des multiples de 2', 'encre', 's')
mat([['2', '0'], ['0', '6']], [['sujet', 'fixe'], ['fixe', 'autre']], 4, 36)
text(ax, 15, 31, r'pivot $d_1=2$ ; reste le 6', 'autre', 's')
arrow(ax, (26, 41), (37, 38), 'autre')
box(ax, 38, 32, 14, 10, 'sujet', label='2')
box(ax, 54, 32, 14, 10, 'fixe', label='2', dash=True)
box(ax, 70, 32, 14, 10, 'fixe', label='2', dash=True)
brace(ax, 38, 84, 43, 'autre', label=r'$6=3\times2$', down=False)
brace(ax, 54, 84, 31, 'varie', label='retrancher 2 fois 2', down=True)
box(ax, 8, 3, 72, 12, 'resultat', label=r'$6-2\times2=2$ : un multiple de $d_1$, donc $2\mid6$', size='s')
save(fig, '59-085')
