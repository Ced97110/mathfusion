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

fig, ax = canvas(54)
text(ax, 20, 48, r'$A$', 'sujet', 'l')
c = mat(ax, 6, 44, 14, 14, [['2', '0'], ['0', '1']], [['sujet', 'fixe'], ['fixe', 'sujet']])
text(ax, 62, 38, r'diagonale : $2\times 1=2$', 'sujet', 's')
text(ax, 62, 28, r'autre : $0\times 0=0$', 'fixe', 's')
text(ax, 62, 14, r'$\det A=2-0=2$', 'resultat', 'm')
save(fig, '71-138')
