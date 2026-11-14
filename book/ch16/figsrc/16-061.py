import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 2, 52, 40, 10, 'sujet', label=r'$x+a=b$'); text(ax, 46, 57, 'départ', 'fixe', 's', ha='left')
arrow(ax, (22, 51), (22, 38), 'varie'); text(ax, 46, 44.5, 'retirer a des deux côtés', 'varie', 's', ha='left')
box(ax, 2, 28, 40, 10, 'fixe', label=r'$x+a-a=b-a$')
arrow(ax, (22, 27), (22, 14), 'varie', lw=1.6); text(ax, 46, 20.5, 'étape clé :\n' + r'$a-a=0$, $x+0=x$', 'varie', 's', ha='left', weight='bold')
box(ax, 2, 4, 40, 10, 'resultat', label=r'$x=b-a$'); text(ax, 46, 9, 'arrivée', 'fixe', 's', ha='left')
save(fig, '16-061')
