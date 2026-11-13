import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 40, r'$[x,y,z]=(xy)z-x(yz)$', 'sujet', 'l')
for i, (l, ra, rb) in enumerate([('x', 'autre', 'fixe'), ('y', 'autre', 'varie'), ('z', 'fixe', 'varie')]):
    box(ax, 8 + 9 * i, 10, 8, 8, ra, label=f'${l}$')
    box(ax, 54 + 9 * i, 10, 8, 8, rb, label=f'${l}$')
text(ax, 44, 14, '−', 'encre', 'xl')
brace(ax, 8, 25, 19.5, 'autre', 'xy d’abord', down=False)
brace(ax, 63, 80, 19.5, 'varie', 'yz d’abord', down=False)
text(ax, 44, 3, 'l’écart entre les deux groupements', 'sujet', 's')
save(fig, '78-052')
