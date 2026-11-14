import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(88)
ox, oy, ux, uy = 8, 38, 8, 3.1
P = lambda x, y: (ox + x * ux, oy + y * uy)
arrow(ax, P(0, 0), (ox + 6.6 * ux, oy), 'fixe', lw=0.7); arrow(ax, P(0, 0), (ox, oy + 13.5 * uy), 'fixe', lw=0.7)
text(ax, ox + 6.6 * ux + 3, oy - 2.5, '$x$', 'fixe', 's'); text(ax, ox - 3, oy + 13.5 * uy, '$y$', 'fixe', 's')
line(ax, [P(0, 1), P(6, 13)], 'sujet', lw=1.4)
for x in (3, 5):
    line(ax, [P(x, 0), P(x, 13.5)], 'varie', dash=True)
    disc(ax, *P(x, 2 * x + 1), 1.3, 'resultat')
    text(ax, P(x, 2 * x + 1)[0] + 2.5, P(x, 2 * x + 1)[1] - 3.5, f'({x}, {2 * x + 1})', 'resultat', 's', ha='left')
box(ax, 10, 17, 58, 14, 'resultat', label=None)
text(ax, 39, 26, 'chaque verticale coupe', 'resultat', 's'); text(ax, 39, 21.5, 'la droite 1 seule fois', 'resultat', 's')
arrow(ax, (39, 17), (39, 12), 'resultat')
box(ax, 14, 2, 50, 9, 'resultat', label='c’est une application', size='m', weight='bold')
save(fig, '42-005')
