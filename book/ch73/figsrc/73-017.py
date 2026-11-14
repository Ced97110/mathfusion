import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(44)
u = 6.5; c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
P = [('rotation', 'sujet', [[c, -s], [s, c]], '1', 7, (-0.8, 1.4)),
     ('dilatation', 'varie', [[2, 0], [0, 1]], '2', 25, (-0.3, 2.3)),
     ('réflexion', 'limite', [[-1, 0], [0, 1]], '−1', 56, (-1.3, 0.4)),
     ('cisaillement', 'resultat', [[1, 1], [0, 1]], '1', 66, (-0.3, 2.3))]
oy = 16
sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
for name, role, M, d, ox, (a, b) in P:
    f = lambda x, y: (ox + u * (M[0][0] * x + M[0][1] * y), oy + u * (M[1][0] * x + M[1][1] * y))
    line(ax, [(ox + a * u, oy), (ox + b * u, oy)], 'fixe', lw=0.5)
    line(ax, [(ox, oy - 2), (ox, oy + 1.7 * u)], 'fixe', lw=0.5)
    poly(ax, [(ox + u * x, oy + u * y) for x, y in sq], 'fixe', fill=False, lw=0.6)
    poly(ax, [f(x, y) for x, y in sq], role)
    xs = [f(x, y)[0] for x, y in sq]
    text(ax, sum(xs) / 4, 35, name, role, 's')
    text(ax, sum(xs) / 4, 6.5, r'$\det=%s$' % d, role, 's')
    ax.add_patch(Circle(f(1, 0), 0.9, fc=COL['encre'], ec=COL['encre'], zorder=6))
    text(ax, f(1, 0)[0], oy - 3.2, 'A', 'encre', 's', weight='bold')
save(fig, '73-017')
