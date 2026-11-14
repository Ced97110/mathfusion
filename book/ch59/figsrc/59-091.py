import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
box(ax, 6, 56, 20, 11, 'sujet', label='A')
arrow(ax, (28, 61.5), (46, 61.5), 'varie', both=True)
box(ax, 48, 56, 16, 11, 'sujet', label='PA')
text(ax, 77, 61.5, r'mêmes $\Delta_i$', 'resultat', 's')
mat([['2', '0'], ['0', '10']], [['sujet', 'fixe'], ['fixe', 'sujet']], 6, 18)
text(ax, 16.5, 45, 'une diagonale', 'sujet', 's')
box(ax, 38, 30, 46, 12, 'resultat', label=r'$\Delta_1=d_1=2$', size='s')
box(ax, 38, 14, 46, 12, 'resultat', label=r'$\Delta_2=d_1d_2=2\times10=20$', size='s')
arrow(ax, (28, 33), (37.5, 36), 'resultat')
arrow(ax, (28, 27), (37.5, 20), 'resultat')
save(fig, '59-091')
