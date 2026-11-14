import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
def mat(x, y, vals, roles, c=8):
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            box(ax, x + j * c, y + (1 - i) * c, c - 0.8, c - 0.8, roles[i][j], label=v)
    line(ax, [(x - 1, y), (x - 2, y), (x - 2, y + 2 * c - 0.8), (x - 1, y + 2 * c - 0.8)], 'encre')
    line(ax, [(x + 2 * c - 0.2, y), (x + 2 * c + 0.8, y), (x + 2 * c + 0.8, y + 2 * c - 0.8), (x + 2 * c - 0.2, y + 2 * c - 0.8)], 'encre')
mat(14, 56, [['2', '1'], ['0', '2']], [['sujet', 'sujet'], ['fixe', 'sujet']])
mat(62, 56, [['2', '0'], ['0', '2']], [['autre', 'fixe'], ['fixe', 'autre']])
text(ax, 22, 76, r'$A$', 'sujet', 'l')
text(ax, 70, 76, r"$A'$", 'autre', 'l')
box(ax, 4, 36, 80, 10, 'fixe', label=r'$f=(\lambda-2)^2$ : le même')
box(ax, 4, 14, 34, 10, 'sujet', label=r'$m=(\lambda-2)^2$', size='s')
box(ax, 50, 14, 34, 10, 'autre', label=r'$m=\lambda-2$', size='s')
text(ax, 44, 19, r'$\neq$', 'limite', 'xl')
arrow(ax, (22, 54), (22, 47), 'fixe'); arrow(ax, (70, 54), (70, 47), 'fixe')
arrow(ax, (22, 35), (22, 25), 'fixe'); arrow(ax, (70, 35), (70, 25), 'fixe')
save(fig, '60-269')
