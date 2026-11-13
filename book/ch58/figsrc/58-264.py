import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# à gauche : module libre -> liste de nombres
text(ax, 22, 69, r'$\mathbb{Z}^2$ : libre', 'sujet', 'm', weight='bold')
box(ax, 7, 50, 30, 10, 'sujet', label='un élément', size='s')
arrow(ax, (22, 49), (22, 40), 'sujet', lw=1.2)
box(ax, 4, 28, 17, 10, 'resultat', label='case 1', size='s')
box(ax, 23, 28, 17, 10, 'resultat', label='case 2', size='s')
text(ax, 22, 20, 'des coordonnées', 'resultat', 's', weight='bold')
# à droite : horloge à 2 heures -> deux écritures
text(ax, 66, 69, 'horloge à 2 heures', 'autre', 'm', weight='bold')
box(ax, 48, 50, 16, 10, 'fixe', label=r'1 $\times$ 1', size='s')
box(ax, 68, 50, 16, 10, 'fixe', label=r'3 $\times$ 1', size='s')
arrow(ax, (56, 49), (63, 40), 'limite', lw=1.2)
arrow(ax, (76, 49), (69, 40), 'limite', lw=1.2)
disc(ax, 66, 34, 5.5, 'limite', label='1', size='l')
text(ax, 66, 22, 'deux écritures de 1', 'limite', 's', weight='bold')
text(ax, 66, 17, 'pas de coordonnées', 'limite', 's')
save(fig, '58-264')
