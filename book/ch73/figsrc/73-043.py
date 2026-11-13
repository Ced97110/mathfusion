import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
c = 9
def grid(x, y, v, hl):
    for i in range(2):
        for j in range(2):
            box(ax, x+j*c, y+(1-i)*c, c, c, 'varie' if (i, j) == hl else 'fixe', label=v[i][j], size='l' if (i, j) == hl else 'm')
grid(8, 10, [['1', '0'], ['0', '1']], None); grid(60, 10, [['1', '3'], ['0', '1']], (0, 1))
text(ax, 17, 33, 'identité', 'fixe', 'm'); text(ax, 69, 33, r'$T_{12}(3)$', 'varie', 'l')
arrow(ax, (28, 19), (57, 19), 'varie')
text(ax, 42, 24, r'$+\,3$ en ligne 1', 'varie', 's'); text(ax, 42, 14, 'colonne 2', 'varie', 's')
text(ax, 44, 4, r'$T_{12}(3) = 1 + 3\, e_{12}$', 'sujet', 'm')
save(fig, '73-043')
