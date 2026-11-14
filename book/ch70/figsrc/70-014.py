import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u, ox, oy = 9.0, 14.0, 14.0
P = lambda x, y: (ox + u * x, oy + u * y)
arrow(ax, P(0, 0), P(4.4, 0), 'fixe', lw=0.7)
arrow(ax, P(0, 0), P(0, 5.8), 'fixe', lw=0.7)
text(ax, P(4.4, 0)[0] + 2.5, oy - 1, r'$x$', 'fixe', 's')
text(ax, ox + 3, P(0, 5.8)[1] + 1, r'$y$', 'fixe', 's')
for v in (1, 2, 3, 4):
    line(ax, [P(v, -0.12), P(v, 0.12)], 'fixe', lw=0.6)
for v in (1, 2, 3, 4, 5):
    line(ax, [P(-0.12, v), P(0.12, v)], 'fixe', lw=0.6)
# the point (3, 5), its fall onto the x axis
disc(ax, *P(3, 5), 1.3, 'sujet')
text(ax, P(3, 5)[0] - 2.5, P(3, 5)[1] + 3.5, r'$(3\,;\,5)$', 'sujet', 's', ha='right')
arrow(ax, (P(3, 5)[0], P(3, 5)[1] - 1.6), (P(3, 0)[0], P(3, 0)[1] + 0.3), 'varie', lw=1.1)
ax.add_patch(Rectangle((P(3, 0)[0] - 1.2, oy - 1.2), 2.4, 2.4, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
text(ax, P(3, 0)[0], oy - 4.5, '3', 'resultat', 's')
text(ax, 58, 40, 'on garde', 'resultat', 's', ha='left')
text(ax, 58, 35, r'$x=3$', 'resultat', 'm', ha='left')
text(ax, 58, 25, "on oublie", 'fixe', 's', ha='left')
text(ax, 58, 20, r'$y=5$', 'fixe', 'm', ha='left')
save(fig, '70-014')
