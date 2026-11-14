import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# ancienne voie : il faut les racines et un dessin
text(ax, 44, 67, 'jusqu’ici : un dessin par équation', 'fixe', 's')
box(ax, 2, 46, 22, 14, 'fixe', label='racines\nconnues', size='s')
box(ax, 33, 46, 22, 14, 'fixe', label='dessin', size='s')
box(ax, 64, 46, 22, 14, 'fixe', label='groupe', size='s')
arrow(ax, (24, 53), (33, 53), 'fixe')
arrow(ax, (55, 53), (64, 53), 'fixe')
# nouvelle voie : coefficients -> d -> groupe
text(ax, 44, 36, 'maintenant : un calcul sur les coefficients', 'sujet', 's')
box(ax, 2, 12, 22, 16, 'sujet', label='coefficients\n1, 0, −3, 1', size='s')
box(ax, 33, 12, 22, 16, 'varie', label='discriminant', size='s')
box(ax, 64, 12, 22, 16, 'resultat', label=r'$A_3$ ou $S_3$', size='m')
arrow(ax, (24, 20), (33, 20), 'sujet')
arrow(ax, (55, 20), (64, 20), 'varie')
save(fig, '65-019')
