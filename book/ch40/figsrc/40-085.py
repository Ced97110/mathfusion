import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# départ
box(ax, 28, 76, 32, 12, 'sujet', label=r'$r=2\cos\theta$', size='m')
# chemin A (long) à gauche, chemin B (court) à droite
text(ax, 12, 87, '3 étapes', 'fixe', 'm')
text(ax, 76, 87, '2 étapes', 'resultat', 'm')
box(ax, 4, 46, 38, 11, 'fixe', label=r'$r=2x/r$', size='s')
box(ax, 4, 26, 38, 11, 'fixe', label=r'$r^2=2x$', size='s')
box(ax, 46, 46, 38, 11, 'resultat', label=r'$r^2=2r\cos\theta$', size='s')
box(ax, 26, 3, 36, 11, 'resultat', label=r'$x^2+y^2=2x$', size='m')
# flèches
arrow(ax, (36, 76), (23, 57), 'fixe')
text(ax, 12, 68.5, 'cos θ → x/r', 'fixe', 's') if False else None
arrow(ax, (23, 46), (23, 37), 'fixe')
text(ax, 31, 41.5, '× r', 'fixe', 's')
arrow(ax, (23, 26), (36, 14), 'fixe')
arrow(ax, (52, 76), (65, 57), 'resultat')
text(ax, 62, 68, '× r', 'resultat', 's', ha='left')
arrow(ax, (65, 46), (53, 14), 'resultat')
text(ax, 71, 28, 'r cos θ → x', 'resultat', 's')
text(ax, 71, 22, 'r² → x² + y²', 'resultat', 's')
text(ax, 23, 21, 'r² → x² + y²', 'fixe', 's') if False else None
text(ax, 26, 68, 'cos θ → x/r', 'fixe', 's', ha='right')
text(ax, 11, 20, 'r² → x²+y²', 'fixe', 's')
save(fig, '40-085')
