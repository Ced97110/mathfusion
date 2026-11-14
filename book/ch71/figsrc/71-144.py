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

fig, ax = canvas(52)
roles = [['sujet' if i == j else 'fixe' for j in range(3)] for i in range(3)]
vals = [[('3', '2', '5')[i] if i == j else '0' for j in range(3)] for i in range(3)]
mat(ax, 4, 46, 11, 11, vals, roles)
text(ax, 20, 8, 'diagonale', 'sujet', 's'); text(ax, 20, 3.5, '0 ailleurs', 'fixe', 's')
arrow(ax, (40, 29), (50, 29), 'fixe')
text(ax, 68, 36, 'diag', 'encre', 'l'); text(ax, 68, 28, '(3, 2, 5)', 'sujet', 'l')
save(fig, '71-144')
