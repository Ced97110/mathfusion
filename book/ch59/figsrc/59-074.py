import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
def mat(vs, rs, x, y, c=9.5, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['4', '6'], ['6', '4']], [['sujet'] * 2] * 2, 3, 16)
mat([['4', '6'], ['2', r'$-2$']], [['fixe'] * 2] * 2, 34, 16)
mat([['2', '0'], ['0', '10']], [['resultat', 'fixe'], ['fixe', 'resultat']], 65, 16)
arrow(ax, (24.5, 26), (32.5, 26), 'varie', both=True)
arrow(ax, (55.5, 26), (63.5, 26), 'varie', both=True)
text(ax, 13.25, 42, 'A', 'sujet', 'l')
text(ax, 75.25, 42, 'forme normale', 'resultat', 's')
save(fig, '59-074')
