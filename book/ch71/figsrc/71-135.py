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
text(ax, 16, 46, r'$A$', 'sujet', 'l'); text(ax, 70, 46, r'$A^T$', 'sujet', 'l')
mat(ax, 4, 42, 12, 11, [['1', '2'], ['0', '3']], [['varie', 'varie'], ['autre', 'autre']])
mat(ax, 54, 42, 12, 11, [['1', '0'], ['2', '3']], [['varie', 'autre'], ['varie', 'autre']])
arrow(ax, (32, 31), (52, 31), 'fixe')
text(ax, 42, 35, 'échange', 'fixe', 's'); text(ax, 42, 27, 'lignes-colonnes', 'fixe', 's')
save(fig, '71-135')
