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

fig, ax = canvas(62)
text(ax, 22, 56, 'colonne 1', 'fixe', 's'); text(ax, 52, 56, 'colonne 2', 'fixe', 's')
rows = [[r'$b_{11}$', r'$b_{12}$'], [r'$b_{21}$', r'$b_{22}$']]
roles = [['fixe', 'resultat'], ['fixe', 'fixe']]
mat(ax, 14, 52, 22, 14, rows, roles)
text(ax, 7, 38, 'ligne 1', 'fixe', 's', ha='center'); text(ax, 7, 24, 'ligne 2', 'fixe', 's')
text(ax, 44, 12, r'$b_{12}=B(e_1,e_2)=3$', 'resultat', 'm')
save(fig, '71-134')
