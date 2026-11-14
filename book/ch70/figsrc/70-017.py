import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 7.0
r3 = 3 ** 0.5
text(ax, 18, 68, r'avant : $x$ et $y$', 'sujet', 'm', weight='bold')
text(ax, 66, 68, r'après : $x$ seul', 'resultat', 'm', weight='bold')
# left : three points, two numbers each
ox, oy = 18.0, 46.0
P = lambda x, y: (ox + u * x, oy + u * y)
arrow(ax, P(-2.3, 0), P(2.3, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -2.6), P(0, 2.2), 'fixe', lw=0.6)
for a, b in [(-r3, 1), (r3, 1), (0, -2)]:
    line(ax, [P(a, b), P(a, 0)], 'varie', lw=0.8, dash=True)
    disc(ax, *P(a, b), 1.2, 'sujet')
# right : the same abscissas on a line
qx = 66.0
arrow(ax, (qx - 17, oy), (qx + 17, oy), 'fixe', lw=0.6)
for a in (-r3, 0, r3):
    ax.add_patch(Rectangle((qx + u * a - 1.1, oy - 1.1), 2.2, 2.2, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
arrow(ax, (38, oy), (46, oy), 'varie', lw=1.1)
text(ax, 42, oy + 4, 'élimination', 'varie', 's')
# lost / gained
box(ax, 4, 6, 38, 16, 'fixe', size='s')
text(ax, 23, 17, 'perdu', 'fixe', 's')
text(ax, 23, 11, 'la hauteur $y$', 'fixe', 's')
box(ax, 46, 6, 38, 16, 'resultat', size='s')
text(ax, 65, 17, 'gagné', 'resultat', 's')
text(ax, 65, 11, 'une équation en $x$', 'resultat', 's')
save(fig, '70-017')
