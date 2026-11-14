import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bx, bw, bh = 44, 40, 11
ys = [60, 34, 8]
box(ax, bx, ys[0], bw, bh, 'sujet', label=r'$E$')
box(ax, bx, ys[1], bw, bh, 'varie', label=r'$F(z)$')
box(ax, bx, ys[2], bw, bh, 'fixe', label=r'$F$')
arrow(ax, (bx + bw / 2, ys[2] + bh + 0.3), (bx + bw / 2, ys[1] - 0.3), 'resultat')
arrow(ax, (bx + bw / 2, ys[1] + bh + 0.3), (bx + bw / 2, ys[0] - 0.3), 'resultat')
text(ax, bx + bw / 2 - 4, (ys[0] + ys[1] + bh) / 2, 'premier cas : abélien', 'resultat', 's', ha='right')
text(ax, bx + bw / 2 - 4, (ys[1] + ys[2] + bh) / 2, 'lemme 1 : abélien', 'resultat', 's', ha='right')
# à gauche : z est un quotient de deux racines, donc dans E
box(ax, 2, 52, 36, 20, 'sujet', label=r'$r$ et $zr$ dans $E$' + '\n' + r'$z=\dfrac{zr}{r}$ dans $E$', size='s')
arrow(ax, (38.5, 62), (43.5, 65.5), 'sujet')
text(ax, 20, 34, 'on intercale', 'varie', 's')
text(ax, 20, 28, r'$F\subset F(z)\subset E$', 'varie', 's')
save(fig, '64-156')
