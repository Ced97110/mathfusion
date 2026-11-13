import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
c = 9
def grid(x, y, one):
    for i in range(2):
        for j in range(2):
            on = (i + 1, j + 1) == one
            box(ax, x+j*c, y+(1-i)*c, c, c, 'sujet' if on else 'fixe', label='1' if on else '0', size='l' if on else 'm')
grid(12, 12, (1, 2)); grid(58, 12, (2, 1))
text(ax, 21, 36, r'$e_{12}$', 'sujet', 'l'); text(ax, 67, 36, r'$e_{21}$', 'sujet', 'l')
text(ax, 44, 21, r'$\neq$', 'limite', 'l')
text(ax, 6, 25.5, 'ligne 1', 'varie', 's', ha='center', rot=90); text(ax, 30, 8, 'colonne 2', 'varie', 's')
text(ax, 52, 16.5, 'ligne 2', 'varie', 's', rot=90); text(ax, 58+c/2, 8, 'colonne 1', 'varie', 's')
save(fig, '73-042')
