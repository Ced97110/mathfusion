import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(66)
mat(ax, 5, 40, [['0', '1'], [r'$-1$', '0']], 8, [['sujet'] * 2] * 2)
text(ax, 13, 44, r'bloc $S$', 'sujet', 's')
text(ax, 13, 18, 'plan : $r=1$', 'sujet', 's')
text(ax, 13, 12, 'un seul bloc', 'sujet', 's')
c = 8.0; x0 = 40; yt = 46
box(ax, x0, yt - 5 * c, 5 * c, 5 * c, 'fixe')
for k in range(2):
    box(ax, x0 + k * 2 * c, yt - (k + 1) * 2 * c, 2 * c, 2 * c, 'sujet', label=r'$S$', size='l')
text(ax, x0 + 2.5 * c, yt - 4.5 * c, 'zéros', 'fixe', 's'); text(ax, x0 + 3.9 * c, yt - 1.1 * c, 'zéros', 'fixe', 's')
brace(ax, x0, x0 + 4 * c, yt + 3, 'sujet', label=r'$r=2$ blocs $S$', down=False)
save(fig, '71-098')
