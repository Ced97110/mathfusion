import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# composer -> multiplier des tableaux
box(ax, 3, 52, 30, 11, 'sujet', label=r'$\eta_2\circ\eta_1$', size='m')
arrow(ax, (34, 57.5), (49, 57.5), 'varie', lw=1.3)
text(ax, 41.5, 62, 'devient', 'varie', 's')
box(ax, 50, 52, 36, 11, 'resultat', label='produit de deux tableaux', size='s')
line(ax, [(3, 44), (85, 44)], 'fixe', lw=0.6, dash=True)
# résoudre -> système
box(ax, 3, 18, 30, 11, 'sujet', label=r'$\eta(x)=y$', size='m')
arrow(ax, (34, 23.5), (49, 23.5), 'varie', lw=1.3)
text(ax, 41.5, 28, 'devient', 'varie', 's')
text(ax, 68, 38, 'un système', 'resultat', 's', weight='bold')
box(ax, 50, 24, 36, 10, 'resultat', label=r'$2x_1+x_2=14$', size='s')
box(ax, 50, 11, 36, 10, 'resultat', label=r'$x_1+3x_2=17$', size='s')
save(fig, '58-265')
