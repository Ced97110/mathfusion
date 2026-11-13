import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role="encre", dx=6.0, dy=5.0, size="m", roles=None):
    n = len(rows); m = len(rows[0]); w = m * dx; h = n * dy
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            text(ax, cx - w / 2 + dx * (j + .5), cy + h / 2 - dy * (i + .5), v, roles[i][j] if roles else role, size)
    for s in (-1, 1):
        x = cx + s * (w / 2 + 0.3)
        line(ax, [(x - s * 1.3, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.3, cy - h / 2)], "fixe", lw=0.9)

fig, ax = canvas(46)
text(ax, 14, 38, r'$x$ en colonne', 'sujet', 's')
box(ax, 8, 8, 12, 26, 'sujet')
text(ax, 14, 26, '3', 'sujet', 'l'); text(ax, 14, 16, '1', 'sujet', 'l')
arrow(ax, (24, 21), (44, 21), 'varie', lw=1.4)
text(ax, 34, 26, r'$x^T$', 'varie', 'm')
text(ax, 34, 15, 'même liste', 'varie', 's')
text(ax, 68, 38, r'$x^T$ en ligne', 'autre', 's')
box(ax, 48, 15, 32, 12, 'autre')
text(ax, 58, 21, '3', 'autre', 'l'); text(ax, 70, 21, '1', 'autre', 'l')
save(fig, '71-058')
