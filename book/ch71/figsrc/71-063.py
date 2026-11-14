import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(62)
box(ax, 26, 48, 36, 11, 'sujet', label='une même forme', size='m')
arrow(ax, (36, 48), (20, 38), 'sujet'); arrow(ax, (52, 48), (68, 38), 'sujet')
text(ax, 20, 33, r'base $(e_i)$', 'sujet', 's'); text(ax, 68, 33, r'base $(u_j)$', 'autre', 's')
mat(ax, 20, 20, [['2   0'], ['0   1']], 'sujet', dx=13, dy=7)
mat(ax, 68, 20, [['3   1'], ['1   3']], 'autre', dx=13, dy=7)
arrow(ax, (34, 20), (54, 20), 'varie', lw=1.3, both=True)
text(ax, 44, 26, r'$P^T A P$', 'varie', 's')
text(ax, 44, 7, 'matrices congruentes', 'resultat', 'm')
save(fig, '71-063')
