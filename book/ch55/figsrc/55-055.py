import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 64, 38, 15, 'fixe', label='relation gardée :\n' + r'$x_1^2 - x_1$', size='s')
box(ax, 48, 64, 38, 15, 'varie', label=r'$g = x_2^2 - x_2$')
for i in range(2):
    for j in range(2):
        box(ax, 6 + i * 8, 36 + j * 8, 8, 8, 'resultat', r=0.3)
text(ax, 26, 40, 'valeur 0\naux 4 couples', 'resultat', 's', ha='left')
arrow(ax, (52, 63), (18, 53.5), 'varie', curve=0.1)
box(ax, 50, 34, 36, 18, 'limite', label=r'$g$ n’est pas un' + '\nmultiple de ' + r'$x_1^2 - x_1$', size='s')
arrow(ax, (68, 63), (68, 53), 'varie')
box(ax, 4, 6, 80, 20, 'limite', label='pas d’isomorphisme :\nquotient infini, 16 fonctions', size='s')
save(fig, '55-055')
