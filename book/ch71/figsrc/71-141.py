import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, cw, ch, rows, roles=None, size='m'):
    """Matrix of boxes, top-left corner (x, y). Returns centers dict (i, j) -> (cx, cy)."""
    c = {}
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            r = roles[i][j] if roles else 'fixe'
            bx, by = x + j * cw, y - (i + 1) * ch
            box(ax, bx + 0.3, by + 0.3, cw - 0.6, ch - 0.6, r, label=v, size=size, r=0.5)
            c[(i, j)] = (bx + cw / 2, by + ch / 2)
    return c

fig, ax = canvas(56)
text(ax, 11, 30, r'$S=$', 'encre', 'xl')
text(ax, 36, 51, r'$e_1$', 'fixe', 'm'); text(ax, 56, 51, r'$e_2$', 'fixe', 'm')
mat(ax, 26, 47, 20, 14, [['0', '1'], ['−1', '0']], [['fixe', 'resultat'], ['varie', 'fixe']], size='l')
text(ax, 20, 40, r'$e_1$', 'fixe', 'm'); text(ax, 20, 26, r'$e_2$', 'fixe', 'm')
text(ax, 44, 11, r'ligne $i$, colonne $j$ : $B(e_i,e_j)$', 'fixe', 's')
save(fig, '71-141')
