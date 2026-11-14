import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# left: x^2 + 1 never touches 0
ox, oy, ux, uy = 22, 14, 10, 6
f = lambda x: oy + (x * x + 1) * uy
arrow(ax, (4, oy), (41, oy), 'fixe', lw=0.8)
xs = [-1.5 + 3 * k / 40 for k in range(41)]
line(ax, [(ox + x * ux, f(x)) for x in xs], 'autre', lw=1.5)
text(ax, 38, oy - 3.5, '0', 'fixe', 's')
text(ax, 22, 8, 'aucun réel x', 'limite', 's')
text(ax, 22, 50, 'x² + 1 = 0', 'autre', 'l', weight='bold')
text(ax, 22, 58, 'équation à résoudre', 'fixe', 's')
# right: T obeys it
box(ax, 55, 26, 22, 14, 'sujet', label='T', size='xl', weight='bold')
text(ax, 66, 50, 'T² + 1 = 0', 'resultat', 'l', weight='bold')
text(ax, 66, 58, 'règle suivie par T', 'fixe', 's')
text(ax, 66, 17, 'vrai pour T', 'resultat', 's')
line(ax, [(44, 8), (44, 58)], 'fixe', lw=0.5, dash=True)
save(fig, '57-015')
