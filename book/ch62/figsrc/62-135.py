import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# forme factorisée -> forme développée : la racine double disparaît de la vue
box(ax, 2, 54, 44, 10, 'sujet', label=r'$(x-1)^2\,(x+2)$')
text(ax, 66, 59, 'racine double : 1', 'resultat', 's')
text(ax, 66, 55, 'bien visible', 'resultat', 's')
arrow(ax, (24, 54), (24, 44), 'varie', lw=1.2)
text(ax, 28, 49, 'développer', 'varie', 's', ha='left')
box(ax, 2, 33, 56, 10, 'fixe', label=r'$(x^2-2x+1)\,(x+2)$')
arrow(ax, (24, 33), (24, 23), 'varie', lw=1.2)
text(ax, 28, 28, 'développer', 'varie', 's', ha='left')
box(ax, 2, 12, 44, 10, 'fixe', label=r'$x^3-3x+2$')
text(ax, 66, 17, 'racine double : ?', 'varie', 's')
save(fig, '62-135')
