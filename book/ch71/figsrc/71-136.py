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

fig, ax = canvas(60)
s = 9.0; o = (16, 30)
arrow(ax, (3, 30), (32, 30), 'fixe'); arrow(ax, (16, 8), (16, 54), 'fixe')
arrow(ax, o, (o[0] + s, o[1] + s), 'sujet', lw=1.5); arrow(ax, o, (o[0] + s, o[1] - s), 'autre', lw=1.5)
text(ax, o[0] + s + 4, o[1] + s + 3, r'$u_1$', 'sujet', 'm'); text(ax, o[0] + s + 4, o[1] - s - 3, r'$u_2$', 'autre', 'm')
text(ax, 67, 51, r'$u_1$', 'sujet', 'm'); text(ax, 80, 51, r'$u_2$', 'autre', 'm')
mat(ax, 54, 47, 13, 11, [['1', '1'], ['1', '−1']], [['sujet', 'autre'], ['sujet', 'autre']])
text(ax, 46, 36, r'$P$', 'encre', 'xl')
save(fig, '71-136')
