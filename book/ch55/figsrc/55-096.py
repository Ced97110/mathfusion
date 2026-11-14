import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'le polynôme symétrique contient', 'fixe', 'm')
bx, bw, bh = 4, 36, 12
box(ax, bx, 38, bw, bh, 'resultat', label=r'$x_1^2x_2$ : $(2,\,1)$', weight='bold')
box(ax, bx, 8, bw, bh, 'fixe', label=r'$x_1x_2^2$ : $(1,\,2)$')
cx = bx + bw / 2
arrow(ax, (cx, 36), (cx, 22), 'varie', both=True)
text(ax, cx + 3, 29, r'échange $x_1\leftrightarrow x_2$', 'varie', 's', ha='left')
text(ax, 46, 47, r'$2\geq 1$ : décroissant', 'resultat', 'm', ha='left', weight='bold')
text(ax, 46, 41, 'le plus haut des deux', 'resultat', 's', ha='left')
text(ax, 46, 14, r'$1<2$ : pas décroissant', 'fixe', 'm', ha='left')
save(fig, '55-096')
