import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
oy = 14
text(ax, 22, 57, 'addition de deux flèches', 'fixe', 's')
text(ax, 66, 57, 'nombre fois une flèche', 'fixe', 's')
line(ax, [(44, 4), (44, 57)], 'fixe', lw=0.5, dash=True)
# left: sum of two arrows
u = 9; ox = 17
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-1, 0), P(2.4, 0), 'fixe', lw=0.6); arrow(ax, P(0, 0), P(0, 3.6), 'fixe', lw=0.6)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.5); arrow(ax, P(0, 0), P(-1, 2), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(1, 3), 'resultat', lw=1.7)
text(ax, *P(2.15, 0.7), 'v', 'sujet', 'm', ha='left', weight='bold')
text(ax, *P(-1.2, 2.2), 'w', 'autre', 'm', ha='right', weight='bold')
text(ax, *P(1.2, 3.3), 'v + w', 'resultat', 'm', ha='left', weight='bold')
text(ax, 22, 5, 'deux flèches → une flèche', 'resultat', 's')
# right: number times arrow
u2 = 7.5; ox2 = 52
Q = lambda x, y: (ox2 + x * u2, oy + y * u2)
arrow(ax, Q(0, 0), Q(4.5, 0), 'fixe', lw=0.6); arrow(ax, Q(0, 0), Q(0, 2.6), 'fixe', lw=0.6)
arrow(ax, Q(0, 0), Q(4, 2), 'varie', lw=1.6); arrow(ax, Q(0, 0), Q(2, 1), 'sujet', lw=1.8)
text(ax, *Q(2.4, 0.5), 'v', 'sujet', 'm', weight='bold')
text(ax, *Q(3.2, 2.2), '2 × v', 'varie', 'm', weight='bold')
text(ax, 66, 5, 'un nombre, une flèche → une flèche', 'resultat', 's')
save(fig, '57-029')
