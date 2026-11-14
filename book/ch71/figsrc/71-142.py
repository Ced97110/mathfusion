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

fig, ax = canvas(48)
text(ax, 15, 41, 'alternée', 'fixe', 's')
mat(ax, 3, 38, 12, 12, [['0', '3'], ['−3', '0']], [['fixe', 'sujet'], ['fixe', 'fixe']])
arrow(ax, (29, 26), (37, 26), 'varie'); text(ax, 33, 31, 'Pf', 'varie', 's')
box(ax, 37, 17, 16, 18, 'resultat', label='3', size='l')
arrow(ax, (53, 26), (61, 26), 'varie'); text(ax, 57, 31, 'carré', 'varie', 's')
box(ax, 61, 17, 24, 18, 'autre', label=r'$9=\det$', size='m')
text(ax, 44, 8, r'$\mathrm{Pf}^2=\det$', 'encre', 'm')
save(fig, '71-142')
