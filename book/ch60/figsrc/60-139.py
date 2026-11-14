import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, ytop, cw, ch = 16, 66, 14, 9
for i in range(4):
    for j in range(2):
        if (i, j) == (3, 1): role = 'resultat'
        elif (i, j) == (0, 1): role = 'varie'
        elif j == 0: role = 'sujet'
        else: role = 'fixe'
        box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=f'({i}, {j})', size='s', r=0.5)
# 3 x g : down along column 0
arrow(ax, (x0 - 3, ytop - 0.5 * ch), (x0 - 3, ytop - 3.5 * ch), 'sujet')
text(ax, 6, ytop - 2 * ch, r'$3 \times g$', 'sujet', 's')
# + y : across the bottom row
yb = ytop - 4 * ch
arrow(ax, (x0 + 0.5 * cw, yb - 3), (x0 + 1.5 * cw, yb - 3), 'varie')
text(ax, x0 + cw, yb - 7.5, r'$+\ y$,  $y = (0, 1)$', 'varie', 's')
tx = 50
text(ax, tx, 58, 'x = (3, 1)', 'resultat', 'm', ha='left', weight='bold')
text(ax, tx, 48, r'$x = 3 \times g + y$', 'encre', 's', ha='left')
text(ax, tx, 41, r'$(3, 1) = (3, 0) + (0, 1)$', 'encre', 's', ha='left')
text(ax, tx, 32, r'$y$ est dans $K$', 'varie', 's', ha='left')
text(ax, tx, 22, r'$G = \langle g\rangle \oplus K$', 'resultat', 'm', ha='left', weight='bold')
save(fig, '60-139')
