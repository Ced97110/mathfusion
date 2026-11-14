import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# gauche : x^3 - 2, trois racines distinctes
text(ax, 21, 64, r'$x^3-2$ : $d=3$', 'resultat', 's')
for k, lab in enumerate([r'$r$', r'$jr$', r'$j^2r$']):
    box(ax, 5, 44 - k * 15, 32, 12, 'resultat', label=lab, size='s')
text(ax, 21, 4, r'3 choix $=d$', 'resultat', 's')
# droite : (x-1)^2, une seule racine
text(ax, 67, 64, r'$(x-1)^2$ : $d=2$', 'limite', 's')
box(ax, 46, 44, 18, 12, 'fixe', label=r'$x-1$', size='s')
box(ax, 68, 44, 18, 12, 'fixe', label=r'$x-1$', size='s')
arrow(ax, (55, 43.5), (63, 33.5), 'varie')
arrow(ax, (77, 43.5), (71, 33.5), 'varie')
box(ax, 56, 21, 24, 12, 'limite', label=r'racine $1$', size='s')
text(ax, 67, 4, r'1 choix $<d$', 'limite', 's')
save(fig, '63-096')
