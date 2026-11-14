import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['2', '0'], ['0', '10']], [['sujet', 'fixe'], ['fixe', 'sujet']], 24, 22)
text(ax, 11, 38, r'$d_1=2$', 'sujet', 'm')
arrow(ax, (17.5, 38), (23.5, 38), 'sujet')
text(ax, 60, 27, r'$d_2=10$', 'sujet', 'm')
arrow(ax, (54.5, 27), (46.5, 27), 'sujet')
text(ax, 44, 14, r'$d_i$ : le $i$-ième nombre', 'sujet', 's')
text(ax, 44, 6, r'$d_i\mid d_{i+1}$ : 2 divise 10', 'resultat', 's')
save(fig, '59-067')
