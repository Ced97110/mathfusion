import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['4', '6'], ['6', '4']], [['sujet'] * 2] * 2, 4, 22)
text(ax, 14.5, 50, 'A', 'sujet', 'l')
text(ax, 62, 55, 'ordre 1 : quatre mineurs', 'sujet', 's')
for i, v in enumerate(['4', '6', '6', '4']):
    box(ax, 38 + i * 12, 40, 11, 11, 'sujet', label=v)
arrow(ax, (26, 38), (36, 44), 'sujet')
box(ax, 50, 14, 34, 12, 'autre', label=r'$4\times4-6\times6=-20$', size='s')
arrow(ax, (26, 28), (49, 22), 'autre')
text(ax, 67, 9, 'ordre 2 : un seul mineur', 'autre', 's')
save(fig, '59-087')
