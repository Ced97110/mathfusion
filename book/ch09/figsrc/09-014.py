import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u, ox, oy = 6.5, 9, 9
P = lambda a, b: (ox + a * u, oy + b * u)
box(ax, ox, oy, 4 * u, 3 * u, 'sujet', r=0.3)
box(ax, ox, oy, 8 * u, 6 * u, 'autre', fill=False, r=0.3, lw=1.0)
box(ax, ox, oy, 8 * u, 5 * u, 'limite', fill=False, dash=True, r=0.3, lw=0.9)
line(ax, [P(0, 0), P(8.6, 6.45)], 'varie', lw=1.3)
for q, role in [((0, 0), 'fixe'), ((4, 3), 'sujet'), ((8, 6), 'autre'), ((8, 5), 'limite')]:
    disc(ax, *P(*q), 1.1, role)
text(ax, ox - 3, oy - 3, r'$O$', 'encre', 'm')
text(ax, P(4, 3)[0] - 3.5, P(4, 3)[1] + 3, r'$P$', 'sujet', 'm')
text(ax, P(8, 6)[0] - 3.5, P(8, 6)[1] + 3.5, r'$Q$', 'autre', 'm', weight='bold')
text(ax, P(2, 0)[0], oy - 3, '4', 'sujet', 's'); text(ax, P(6, 0)[0], oy - 3, '8', 'autre', 's')
text(ax, ox - 3, P(0, 1.5)[1], '3', 'sujet', 's'); text(ax, ox - 3, P(0, 6)[1], '6', 'autre', 's'); text(ax, ox - 3, P(0, 5)[1], '5', 'limite', 's')
text(ax, P(8, 5)[0] + 2.5, P(8, 5)[1] - 10, 'hauteur 5 :', 'limite', 's', ha='right')
text(ax, P(8, 5)[0] + 2.5, P(8, 5)[1] - 14, 'hors de la droite', 'limite', 's', ha='right')
text(ax, 44, 61, 'coins alignés avec O', 'encre', 's')
save(fig, '09-014')
