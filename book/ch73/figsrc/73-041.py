import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(46)
u = 6.0; by = 19
def tri(cx, M, role):
    P = [(0, 0), (1, 0), (1, 1), (0, 1)]
    Q = [(cx + u*(M[0][0]*x + M[0][1]*y), by + u*(M[1][0]*x + M[1][1]*y)) for x, y in P]
    xs = [q[0] for q in Q]; sh = cx - (min(xs) + max(xs)) / 2
    Q = [(q[0] + sh, q[1]) for q in Q]
    poly(ax, Q, role)
    disc(ax, Q[1][0], Q[1][1], 1.0, 'varie'); disc(ax, Q[3][0], Q[3][1], 1.0, 'autre')
c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
cols = [(9, [[1, 0], [0, 1]], 'sujet', 'départ', ''),
        (27, [[c, -s], [s, c]], 'resultat', 'rotation 30°', 'det 1'),
        (44, [[1, 1], [0, 1]], 'resultat', 'cisaillement', 'det 1'),
        (60, [[-1, 0], [0, 1]], 'limite', 'réflexion', r'det $-1$'),
        (76, [[2, 0], [0, 1]], 'limite', 'dilatation ×2', 'det 2')]
for cx, M, role, nm, d in cols:
    tri(cx, M, role)
    text(ax, cx, 10, nm, role, 's')
    if d: text(ax, cx, 5, d, role, 's')
text(ax, 44, 40, r'$SL_2(\mathbb{R})$ : $\det = 1$', 'sujet', 'l')
text(ax, 44, 34, 'orange puis violet : même sens', 'fixe', 's')
save(fig, '73-041')
