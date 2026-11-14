import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 8, 35, 10
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox, oy), (ox + 7.2 * u, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 2.8 * u), (ox, oy + 2.8 * u), 'fixe', lw=0.7)
for a, b, r in [(2, 1, 'sujet'), (2, -1, 'autre')]:
    q = P(a, b)
    arrow(ax, (ox, oy), q, r, lw=1.0)
    disc(ax, q[0], q[1], 1.2, r)
# second vector moved to the tip of the first
arrow(ax, P(2, 1), P(4, 0), 'autre', lw=0.8)
line(ax, [P(2, -1), P(4, 0)], 'fixe', dash=True, lw=0.7)
disc(ax, P(4, 0)[0], P(4, 0)[1], 1.5, 'resultat')
text(ax, P(2, 1)[0] - 1, P(2, 1)[1] + 4, r'$2+i$', 'sujet')
text(ax, P(2, -1)[0] - 1, P(2, -1)[1] - 4, r'$2-i$', 'autre')
text(ax, P(4, 0)[0] + 2, P(4, 0)[1] + 4.5, r'$4$', 'resultat', 'l', ha='left')
text(ax, 62, 62, r'partie imaginaire : $1$', 'sujet', ha='center')
text(ax, 62, 55, r'partie imaginaire : $-1$', 'autre', ha='center')
text(ax, 62, 13, r'somme : partie imaginaire $0$', 'resultat', ha='center')
save(fig, '39-122')
