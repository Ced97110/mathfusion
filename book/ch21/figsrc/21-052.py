import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# gauche : x - 2
box(ax, 4, 38, 11, 11, 'sujet', label=r'$x$', size='l')
text(ax, 21, 43.5, r'$-$', 'varie', 'l')
box(ax, 26, 38, 11, 11, 'fixe', label='2', size='l')
brace(ax, 4, 37, 36, 'sujet', label='terme : relié par −', depth=1.6)
# droite : 3x
box(ax, 50, 38, 11, 11, 'fixe', label='3', size='l')
text(ax, 67, 43.5, r'$\times$', 'varie', 'l')
box(ax, 72, 38, 11, 11, 'sujet', label=r'$x$', size='l')
brace(ax, 50, 83, 36, 'sujet', label='facteur : relié par ×', depth=1.6)
text(ax, 44, 63, r'pour $x=5$', 'varie', 'm')
arrow(ax, (20, 23), (20, 18), 'varie')
arrow(ax, (67, 23), (67, 18), 'varie')
box(ax, 6, 6, 28, 11, 'resultat', label=r'$x-2=3$', size='m')
box(ax, 53, 6, 28, 11, 'resultat', label=r'$3x=15$', size='m')
save(fig, '21-052')
