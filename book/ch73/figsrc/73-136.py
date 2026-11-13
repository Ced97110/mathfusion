import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
ones = [(0, 1), (1, 2), (2, 0)]; c = 9
def grid(x0, cells, hl):
    for i in range(3):
        for j in range(3):
            on = (i, j) in cells
            ax.add_patch(Rectangle((x0 + j * c, 14 + (2 - i) * c), c, c, ec=COL['fixe'], fc=FILL['sujet'] if on else 'white', lw=0.7, zorder=2))
    kind, n = hl
    if kind == 'row': ax.add_patch(Rectangle((x0, 14 + (2 - n) * c), 3 * c, c, ec=COL['varie'], fc='none', lw=1.8, zorder=3))
    else: ax.add_patch(Rectangle((x0 + n * c, 14), c, 3 * c, ec=COL['varie'], fc='none', lw=1.8, zorder=3))
grid(6, ones, ('row', 0)); grid(55, [(j, i) for i, j in ones], ('col', 0))
text(ax, 19.5, 46, r'$A$', 'sujet', 'l'); text(ax, 68.5, 46, r'$A^t$', 'autre', 'l')
arrow(ax, (36, 33), (53, 33), 'varie'); text(ax, 44.5, 37, 'ligne → colonne', 'varie', 's')
text(ax, 44, 7, 'case pleine = 1, vide = 0', 'fixe', 's')
save(fig, '73-136')
