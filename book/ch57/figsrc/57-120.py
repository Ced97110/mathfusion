import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
# deux collections, une flèche dans chaque sens
box(ax, 2, 74, 20, 18, 'sujet', label='$R_L$', size='l')
box(ax, 66, 74, 20, 18, 'autre', label='$R_R$', size='l')
arrow(ax, (22.8, 87), (65.2, 87), 'varie', lw=1.2)
arrow(ax, (65.2, 79), (22.8, 79), 'varie', lw=1.2)
text(ax, 44, 91, 'centralisateur de $R_L$', 'varie', 's')
text(ax, 44, 75, 'centralisateur de $R_R$', 'varie', 's')
# la preuve : départ, étape clé, arrivée
box(ax, 2, 52, 84, 12, 'fixe', label='départ : η commute avec tout $R_L$', size='s')
arrow(ax, (44, 51.5), (44, 46.5), 'varie')
box(ax, 2, 28, 84, 17, 'varie', lw=1.6, size='s',
    label='étape clé : η($x$) = η($x$·1)\n= $x$·η(1)')
arrow(ax, (44, 27.5), (44, 22.5), 'varie')
box(ax, 2, 2, 84, 20, 'resultat', size='m', weight='bold',
    label='η est dans $R_R$ :\nmultiplication à droite par η(1)')
save(fig, '57-120')
