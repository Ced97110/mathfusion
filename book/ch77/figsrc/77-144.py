import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 2, 82, 40, 10, 'sujet', label=r'$5=4+1+0$', size='s'); box(ax, 46, 82, 40, 10, 'sujet', label=r'$11=9+1+1$', size='s')
arrow(ax, (22, 81), (36, 72), 'sujet'); arrow(ax, (66, 81), (52, 72), 'sujet')
box(ax, 24, 62, 40, 10, 'sujet', label=r'$5\times11=55$', size='m')
arrow(ax, (44, 61), (44, 54), 'varie')
text(ax, 44, 50, 'sommes de 3 carrés parmi :', 'fixe', 's')
box(ax, 2, 38, 84, 9, 'fixe', label='0   1   4   9   16   25   36   49', size='s')
arrow(ax, (44, 37), (44, 31), 'varie')
box(ax, 8, 20, 72, 10, 'limite', label='aucune somme de 3 = 55', size='m')
text(ax, 44, 13.5, 'nombres de carrés possibles :', 'resultat', 's')
for k, (v, ro) in enumerate([('1', 'resultat'), ('2', 'resultat'), ('3', 'limite'), ('4', 'resultat'), ('8', 'resultat')]):
    box(ax, 6 + k * 16.5, 1, 13, 9, ro, label=v, size='m')
save(fig, '77-144')
