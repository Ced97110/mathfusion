import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['2', '0'], ['0', '12']], [['sujet', 'fixe'], ['fixe', 'sujet']], 4, 24)
text(ax, 14.5, 50, 'forme normale de A', 'sujet', 's')
box(ax, 38, 42, 48, 12, 'fixe', label=r'déterminant : $2\times12=24$', size='s')
box(ax, 38, 22, 48, 12, 'sujet', label=r'$d_1=2$ et $d_2=12$', size='m')
arrow(ax, (26, 38), (37.5, 47), 'fixe')
arrow(ax, (26, 33), (37.5, 28), 'sujet')
text(ax, 38, 38, 'un seul nombre', 'fixe', 's', ha='left')
text(ax, 62, 16, 'la liste entière', 'sujet', 's')
save(fig, '59-075')
