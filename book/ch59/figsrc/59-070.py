import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
vs = [['2', '0', '0'], ['0', '6', '0'], ['0', '0', '0']]
rs = [['sujet', 'fixe', 'fixe'], ['fixe', 'sujet', 'fixe'], ['fixe', 'fixe', 'fixe']]
mat(vs, rs, 28, 14)
text(ax, 33, 50, r'$d_1=2$', 'sujet', 's')
text(ax, 44, 50, r'$d_r=6$', 'sujet', 's')
text(ax, 55, 50, 'zéro', 'fixe', 's')
brace(ax, 50, 60, 13, 'fixe', label='puis des zéros', down=True, size='s')
save(fig, '59-070')
