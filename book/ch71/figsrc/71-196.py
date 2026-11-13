import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def mat(x, y, role):
    for i in range(2):
        for j in range(2): box(ax, x + j * 11, y + (1 - i) * 11, 11, 11, role, label='0', size='l')
mat(6, 34, 'sujet'); mat(56, 34, 'resultat')
arrow(ax, (31, 45), (53, 45), 'varie', lw=1.2)
text(ax, 42, 51, r'$P^T A P$', 'varie', 'm'); text(ax, 42, 39, r'$P$ quelconque', 'varie', 's')
text(ax, 17, 62, r'$A$ (forme nulle)', 'sujet', 's'); text(ax, 67, 62, 'toujours nulle', 'resultat', 's')
box(ax, 4, 4, 38, 14, 'fixe'); text(ax, 23, 11, r'radical $=V$ entier', 'fixe', 's')
box(ax, 46, 4, 38, 14, 'fixe'); text(ax, 65, 11, 'rang 0 : toute base', 'fixe', 's')
save(fig, '71-196')
