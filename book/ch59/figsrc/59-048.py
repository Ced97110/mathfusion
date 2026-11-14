import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
def mat(x, rows, roles):
    for i, vals in enumerate(rows):
        for j, v in enumerate(vals):
            box(ax, x + j * 11, 28 - i * 10, 11, 10, roles[i][j], label=v)
mat(7, [('2', '0'), ('0', '1')], [['sujet'] * 2] * 2)
mat(58, [(r'$\frac{1}{2}$', '0'), ('0', '1')], [['limite', 'fixe'], ['fixe', 'fixe']])
text(ax, 18, 46, r'$\mathrm{diag}(2,1)$', 'sujet', 'm')
text(ax, 69, 46, 'inverse', 'encre', 'm')
arrow(ax, (31, 28), (56, 28), 'varie', lw=1.2)
text(ax, 18, 14, r'$\det=2\neq\pm1$', 'limite', 's')
text(ax, 69, 14, r'$\frac{1}{2}\notin\mathbb{Z}$', 'limite', 's')
save(fig, '59-048')
