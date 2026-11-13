import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['6', '4'], ['4', '6']], [['fixe', 'sujet'], ['fixe', 'fixe']], 4, 18)
mat([['4', '6'], ['6', '4']], [['sujet', 'fixe'], ['fixe', 'fixe']], 63, 18)
arrow(ax, (28, 28.5), (60, 28.5), 'varie')
text(ax, 44, 34, 'échange des colonnes', 'varie', 's')
text(ax, 44, 23, 'type III', 'varie', 's')
text(ax, 14.5, 44, 'plus petit : 4', 'sujet', 's')
text(ax, 73.5, 44, 'en position (1, 1)', 'sujet', 's')
save(fig, '59-078')
