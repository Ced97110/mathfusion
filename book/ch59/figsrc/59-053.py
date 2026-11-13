import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(x, rows, roles):
    for i, vals in enumerate(rows):
        for j, v in enumerate(vals):
            box(ax, x + j * 10, 34 - i * 8, 10, 8, roles[i], label=str(v))
mat(14, [(4, 6), (6, 4)], ['fixe', 'sujet'])
mat(60, [(4, 6), (10, 10)], ['fixe', 'varie'])
text(ax, 3, 38, r'$j=1$', 'fixe', 's', ha='left'); text(ax, 3, 30, r'$i=2$', 'sujet', 's', ha='left')
arrow(ax, (36, 38), (58, 30), 'varie', lw=1.2)
text(ax, 47, 44, r'$T_{21}(1)$', 'varie', 'm')
text(ax, 47, 24, '+ 1 × ligne 1', 'varie', 's')
text(ax, 44, 10, r'à droite : colonne $i$ $\to$ colonne $j$', 'fixe', 's')
save(fig, '59-053')
