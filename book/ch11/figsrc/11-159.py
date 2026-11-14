import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 18; x0, y0 = 4, 9
for i in range(2):
    for j in range(2):
        if (i, j) != (1, 0): box(ax, x0 + i * u, y0 + j * u, u, u, 'fixe', r=0.2, lw=0.5)
poly(ax, [(x0 + u, y0), (x0 + 2 * u, y0 + u), (x0 + u, y0 + 2 * u), (x0, y0 + u)], 'resultat')
box(ax, x0 + u, y0, u, u, 'sujet', r=0.2, lw=1.0)
line(ax, [(x0 + u, y0), (x0 + 2 * u, y0 + u)], 'varie', lw=1.8)
text(ax, x0 + 1.5 * u + 1.5, y0 + 0.28 * u, 'côté 1', 'sujet', 's', rot=0)
text(ax, x0 + u, y0 + 1.15 * u, 'aire 2', 'resultat', 's')
text(ax, 48, 46, 'diagonale d', 'varie', 's', ha='left')
text(ax, 48, 38, r'$d\times d = 2$', 'resultat', 'm', ha='left')
text(ax, 48, 28, r'$1{,}41^2 = 1{,}9881$', 'limite', 's', ha='left')
text(ax, 48, 21, r'$1{,}42^2 = 2{,}0164$', 'limite', 's', ha='left')
text(ax, 48, 12, r'$d = \sqrt{2}$', 'resultat', 'l', ha='left', weight='bold')
save(fig, '11-159')
