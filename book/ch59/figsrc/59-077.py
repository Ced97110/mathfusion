import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['0', '0'], ['0', '0']], [['fixe'] * 2] * 2, 6, 14)
text(ax, 16.5, 40, r'$A=0$', 'sujet', 'l')
arrow(ax, (31, 24.5), (46, 24.5), 'varie')
text(ax, 38.5, 29, 'on s’arrête', 'varie', 's')
box(ax, 50, 19, 32, 12, 'resultat', label=r'$r=0$', size='l')
text(ax, 66, 13, 'aucun nombre non nul', 'resultat', 's')
text(ax, 16.5, 8, 'déjà diagonal', 'fixe', 's')
save(fig, '59-077')
