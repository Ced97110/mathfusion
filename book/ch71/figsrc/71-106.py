import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, ytop, vals, c, roles, size='m'):
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            r = roles[i][j]
            box(ax, x + j * c, ytop - (i + 1) * c, c, c, r or 'fixe', fill=r is not None,
                label=v if v else None, size=size, r=0.3, lw=0.6)
fig, ax = canvas(80)
text(ax, 44, 76, 'même rang, même taille', 'fixe', 's')
box(ax, 3, 6, 39, 64, 'resultat', fill=False, lw=1.0); box(ax, 46, 6, 39, 64, 'limite', fill=False, lw=1.0)
text(ax, 22.5, 65, 'alternées', 'resultat', 'm'); text(ax, 65.5, 65, 'symétriques', 'limite', 'm')
mat(ax, 15.5, 60, [['0', '1'], [r'$-1$', '0']], 7, [['sujet'] * 2] * 2, 's')
text(ax, 22.5, 43, 'toute autre de rang 2', 'resultat', 's'); text(ax, 22.5, 37, 'est congruente à elle', 'resultat', 's')
text(ax, 22.5, 21, 'même rang', 'resultat', 's'); text(ax, 22.5, 15, 'donne congruentes', 'resultat', 's')
mat(ax, 51, 60, [['1', '0'], ['0', '1']], 7, [['sujet'] * 2] * 2, 's')
mat(ax, 51, 42, [['1', '0'], ['0', r'$-1$']], 7, [['autre'] * 2] * 2, 's')
text(ax, 65.5, 44, r'$\neq$', 'limite', 'l')
text(ax, 65.5, 21, 'même rang 2,', 'limite', 's'); text(ax, 65.5, 15, 'non congruentes', 'limite', 's')
save(fig, '71-106')
