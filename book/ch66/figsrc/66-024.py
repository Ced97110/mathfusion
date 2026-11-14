import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 10, 12, 11
box(ax, ox, oy, 72, 48, 'sujet')
arrow(ax, (ox - 3, oy), (ox + 76, oy), 'fixe', lw=0.9); arrow(ax, (ox, oy - 3), (ox, oy + 52), 'fixe', lw=0.9)
text(ax, 73, 53, r'$\mathbb{C}$', 'sujet', 'xl', weight='bold')
A = (ox + 3 * u, oy + 2 * u); B = (ox + 5 * u, oy)
line(ax, [A, (A[0], oy)], 'varie', dash=True); line(ax, [A, (ox, A[1])], 'varie', dash=True)
disc(ax, A[0], A[1], 1.6, 'varie'); disc(ax, B[0], B[1], 1.6, 'resultat')
text(ax, A[0] + 3, A[1] + 3.5, 'abscisse 3,\nordonnée 2', 'varie', 's', ha='left')
text(ax, B[0], B[1] + 6, '5 sur l\'axe\nhorizontal', 'resultat', 's')
text(ax, A[0], oy - 4, '3', 'varie', 's'); text(ax, B[0], oy - 4, '5', 'resultat', 's'); text(ax, ox - 3.5, A[1], '2', 'varie', 's')
text(ax, 44, 4, 'tous les points du plan', 'sujet', 's')
save(fig, '66-024')
