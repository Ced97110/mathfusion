import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# matrice : les lots f1 = (2, 1) et f2 = (1, 1) écrits avec les sacs ; une colonne par lot
text(ax, 44, 57, 'matrice : un seul objet', 'encre', 'm', weight='bold')
text(ax, 38, 47, r'lot $f_1$', 'sujet', 's')
text(ax, 58, 47, r'lot $f_2$', 'autre', 's')
x0, y0, w, h, gx = 28, 14, 18, 14, 2
cells = [[2, 1], [1, 1]]
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * (w + gx), y0 + (1 - r) * (h + gx), w, h, 'sujet' if c == 0 else 'autre',
            label=str(cells[r][c]), size='l', weight='bold')
text(ax, 25, y0 + h + gx + h / 2, r'sacs $e_1$', 'fixe', 's', ha='right')
text(ax, 25, y0 + h / 2, r'sacs $e_2$', 'fixe', 's', ha='right')
# crochets de matrice
xl, xr = x0 - 2.5, x0 + 2 * w + gx + 2.5
for xx, d in [(xl, 1.8), (xr, -1.8)]:
    line(ax, [(xx + d, y0 - 1.5), (xx, y0 - 1.5), (xx, y0 + 2 * h + gx + 1.5), (xx + d, y0 + 2 * h + gx + 1.5)], 'encre', lw=1.0)
text(ax, 44, 5, 'quatre nombres rangés : 2 lignes, 2 colonnes', 'fixe', 's')
save(fig, '58-018')
