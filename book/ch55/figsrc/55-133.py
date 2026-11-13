import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'une seule variable : $r=1$', 'sujet', 'm', weight='bold')
# the only permutation of {1}: it moves nothing (a loop on the point 1)
disc(ax, 16, 50, 4.5, 'sujet', label=r'$1$', size='l')
arrow(ax, (12.5, 54), (19.5, 54), 'varie', curve=-2.2)
text(ax, 16, 36, 'seule permutation :', 'fixe', 's')
text(ax, 16, 31.5, 'rien ne bouge', 'fixe', 's')
# the polynomial is unchanged by renaming
box(ax, 36, 46, 22, 9, 'sujet', label=r'$x_1^2+3$', size='m')
arrow(ax, (58, 50.5), (62, 50.5), 'varie')
box(ax, 62, 46, 22, 9, 'sujet', label=r'$x_1^2+3$', size='m')
text(ax, 60, 59, 'après renommage', 'fixe', 's')
# e1 = x1
box(ax, 4, 14, 80, 9, 'resultat', label=r'$e_1=x_1$, donc $x_1^2+3=e_1^2+3$', size='m')
text(ax, 60, 27, 'vrai, mais vide', 'fixe', 's')
save(fig, '55-133')
