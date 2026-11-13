import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def grid(x0, y0, c, heads, hl, val, role):
    for i in range(4):
        for j in range(4):
            box(ax, x0 + (j + 1) * c, y0 + (3 - i) * c, c, c, 'fixe', fill=False, lw=0.5, r=0.2)
        text(ax, x0 + c / 2, y0 + (3 - i) * c + c / 2, heads[i], role, 's')
        text(ax, x0 + (i + 1) * c + c / 2, y0 + 4 * c + c / 2, heads[i], role, 's')
    i, j = hl
    box(ax, x0 + (j + 1) * c, y0 + (3 - i) * c, c, c, 'resultat', fill=True, lw=0.9, r=0.2, label=val, size='s')
grid(3, 18, 7.5, ['1', '2', '3', '4'], (2, 3), r'12', 'fixe')
grid(46, 18, 7.5, ['1', r'$r$', r'$r^{2}$', r'$r^{3}$'], (1, 2), r'$r^{3}$', 'sujet')
text(ax, 22, 8, 'ligne 3, colonne 4', 'fixe', 's')
text(ax, 66, 8, r'ligne $r$, colonne $r^{2}$', 'sujet', 's')
text(ax, 22, 59, 'nombres : produit', 'fixe', 's'); text(ax, 66, 59, 'monoïde : composée', 'sujet', 's')
save(fig, '44-093')
