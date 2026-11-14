import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
def mat(x, y, cells, role, cs=7, lw=0.8):
    """2x2 grid, top-left corner of the top row at (x, y + cs); cell (0,0) is top-left."""
    for i in range(2):
        for j in range(2):
            on = (i, j) in cells
            ax.add_patch(Rectangle((x + j * cs, y - i * cs), cs, cs, ec=COL[role], fc=FILL[role] if on else 'white', lw=lw, zorder=2))
text(ax, 44, 92, 'cadran à 2 heures : un cas', 'encre', 's')
text(ax, 44, 87, 'case pleine = 1, vide = 0', 'fixe', 's')
mat(6, 73, {(0, 0)}, 'sujet')
text(ax, 24, 70, '×', 'encre', 'l')
mat(31, 73, {(1, 1)}, 'autre')
text(ax, 49, 70, '=', 'encre', 'l')
mat(55, 73, set(), 'limite')
text(ax, 13, 61, '1er', 'sujet', 's')
text(ax, 38, 61, '2e', 'autre', 's')
text(ax, 62, 61, 'produit nul', 'limite', 's')
line(ax, [(4, 55), (84, 55)], 'fixe', lw=0.5)
text(ax, 44, 50, 'les 16 tableaux possibles', 'encre', 's', weight='bold')
first, second = {(0, 0)}, {(1, 1)}
for k in range(16):
    cells = {(i, j) for i, j, b in ((0, 0, 3), (0, 1, 2), (1, 0, 1), (1, 1, 0)) if (k >> b) & 1}
    role = 'sujet' if cells == first else ('autre' if cells == second else 'fixe')
    r, c = divmod(k, 8)
    mat(3.5 + c * 10.6, 42 - r * 12, cells, role, cs=4, lw=0.6)
text(ax, 44, 17, 'tableaux inversibles : combien ?', 'encre', 's')
text(ax, 44, 8, 'diviseurs de zéro : combien ?', 'encre', 's')
save(fig, '51-286')
