import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, ytop, cw, ch = 4, 66, 14, 9
for i in range(4):
    for j in range(2):
        if (i, j) == (1, 1): role = 'limite'
        elif (i, j) == (0, 1): role = 'resultat'
        elif j == 0: role = 'sujet'
        else: role = 'fixe'
        lw = 1.8 if (i, j) == (1, 0) else 0.8
        box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=f'({i}, {j})', size='s', lw=lw, r=0.5)
xr = x0 + 2 * cw + 0.8
arrow(ax, (xr, ytop - 1.5 * ch), (xr, ytop - 0.5 * ch), 'varie', curve=1.2)
text(ax, xr + 5, ytop - ch, '− g', 'varie', 's', ha='left')
tx = 47
text(ax, tx, 60, 'mauvais choix', 'limite', 's', ha='left', weight='bold')
text(ax, tx, 55, 'h = (1, 1), ordre 4', 'limite', 's', ha='left')
text(ax, tx, 46, r'$2h = (2, 0) = 2 \times g$', 'fixe', 's', ha='left')
text(ax, tx, 40, r'$r = 2$, $s = 1$', 'varie', 's', ha='left')
text(ax, tx, 31, r'$a = (1, 1) - (1, 0)$', 'encre', 's', ha='left')
text(ax, tx, 25, r'$a = (0, 1)$, ordre 2', 'resultat', 's', ha='left', weight='bold')
text(ax, 20, 14, 'g = (1, 0) : bord épais', 'sujet', 's')
save(fig, '60-134')
