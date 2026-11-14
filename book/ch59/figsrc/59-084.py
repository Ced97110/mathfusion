import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['2', '0'], ['0', '10']], [['sujet', 'fixe'], ['fixe', 'varie']], 30, 18)
text(ax, 35, 46, r'$d_1$ : isolé d’abord', 'sujet', 's')
text(ax, 46, 11, r'$d_2$ : isolé ensuite', 'varie', 's')
text(ax, 72, 33, r'$d_1\mid d_2$', 'resultat', 'l')
text(ax, 72, 26, '2 divise 10', 'resultat', 's')
save(fig, '59-084')
