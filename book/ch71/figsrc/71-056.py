import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(52)
cw, ch = 25, 10
vals = [[2, 0], [0, 1]]
for i in range(2):
    for j in range(2):
        r = 'resultat' if vals[i][j] else 'fixe'
        box(ax, 4 + j * (cw + 1), 28 - i * (ch + 1), cw, ch, r, label=r'$B(e_%d,e_%d) = %d$' % (i + 1, j + 1, vals[i][j]), size='s')
arrow(ax, (57, 28), (65, 28), 'varie', lw=1.3)
text(ax, 61, 36, 'on range', 'varie', 's')
mat(ax, 75, 28, [['2', '0'], ['0', '1']], roles=[['resultat', 'fixe'], ['fixe', 'resultat']], dx=6.5, dy=7)
text(ax, 75, 11, r'$A = (b_{ij})$', 'sujet', 'm')
text(ax, 28, 46, r'$b_{ij} = B(e_i,\,e_j)$', 'sujet', 'm')
save(fig, '71-056')
