import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['4', '6'], ['6', '4']], [['sujet', 'fixe'], ['fixe', 'fixe']], 4, 22)
mat([['4', '2'], ['2', r'$-4$']], [['sujet', 'varie'], ['varie', 'fixe']], 62, 22)
arrow(ax, (28, 32.5), (58, 32.5), 'varie')
text(ax, 43, 38, r'$6=1\times4+2$', 'varie', 's')
text(ax, 43, 27, 'on retranche', 'varie', 's')
text(ax, 14.5, 15, 'pivot 4', 'sujet', 's')
text(ax, 72.5, 15, r'restes $2<4$', 'varie', 's')
text(ax, 44, 52, 'division euclidienne répétée', 'encre', 's')
save(fig, '59-076')
