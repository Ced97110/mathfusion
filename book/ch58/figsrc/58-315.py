import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 4.6
oxl, oyl = 20, 38
oxr, oyr = 66, 34
pl = lambda x, y: (oxl + x * u, oyl + y * u)
pr = lambda x, y: (oxr + x * u, oyr + y * u)
text(ax, 44, 62, 'A : colonnes (1, 2) et (2, 4)', 'encre', 's')
# plan de départ : la droite du noyau
line(ax, [pl(-3, 1.5), pl(3.2, -1.6)], 'sujet', lw=1.6)
arrow(ax, pl(0, 0), pl(2, -1), 'sujet', lw=1.6)
text(ax, 20, 53, 'noyau : droite de (2, −1)', 'sujet', 's')
# plan d'arrivée : la droite de l'image
line(ax, [pr(-1.2, -2.4), pr(1.4, 2.8)], 'resultat', lw=1.6)
arrow(ax, pr(0, 0), pr(1, 2), 'resultat', lw=1.6)
text(ax, 66, 53, 'image : droite de (1, 2)', 'resultat', 's')
arrow(ax, (38, 40), (50, 40), 'encre', lw=1.0)
text(ax, 44, 44, r'$\eta$', 'encre', 'm')
box(ax, 3, 24, 34, 26, 'fixe', fill=False, lw=0.5)
box(ax, 50, 21, 32, 27, 'fixe', fill=False, lw=0.5)
# dimensions : 1 + 1 = 2
text(ax, 44, 20, 'dim V = 2', 'encre', 's')
box(ax, 16, 4, 28, 10, 'sujet', label='noyau : 1', size='s')
box(ax, 44, 4, 28, 10, 'resultat', label='image : 1', size='s')
save(fig, '58-315')
