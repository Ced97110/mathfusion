import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
c = 9; mx, my = 33, 14
box(ax, 2, 20, 22, 10, 'sujet', label=r'$a \in F^*$')
arrow(ax, (25, 25), (31, 25), 'varie')
vals = [['a', '0'], ['0', '1']]
for i in range(2):
    for j in range(2):
        role = 'sujet' if (i, j) == (0, 0) else ('fixe' if vals[i][j] == '0' else 'autre')
        box(ax, mx+j*c, my+(1-i)*c, c, c, role, label=vals[i][j] if vals[i][j] != 'a' else r'$a$')
text(ax, mx+c, 36, 'matrice diagonale', 'sujet', 's')
arrow(ax, (mx+2*c+2, 23), (mx+2*c+8, 23), 'varie')
box(ax, 66, 17, 20, 12, 'resultat', label=r'det $= a$')
text(ax, 76, 11, r'$a \times 1 = a$', 'resultat', 's')
text(ax, 44, 4, 'chaque $a$ non nul est atteint', 'resultat', 's')
save(fig, '73-034')
