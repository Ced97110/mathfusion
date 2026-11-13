import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
box(ax, 4, 22, 30, 12, 'sujet', label='diag(2, 10)')
text(ax, 41, 28, '=', 'encre', 'l')
mat([['2', '0'], ['0', '10']], [['sujet', 'fixe'], ['fixe', 'sujet']], 48, 17.5)
text(ax, 19, 14, 'on écrit : 2 et 10', 'sujet', 's')
text(ax, 58.5, 11, 'les zéros : sous-entendus', 'fixe', 's')
save(fig, '59-066')
