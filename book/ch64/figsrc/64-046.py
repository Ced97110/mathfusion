import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
r = 3.2
def link(p, q, role, both=False, curve=0.0):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * (r + 0.5), p[1] + u[1] * (r + 0.5)), (q[0] - u[0] * (r + 0.5), q[1] - u[1] * (r + 0.5)), role, both=both, curve=curve)
P = {1: (10, 32), 2: (30, 32), 3: (20, 49)}
for a, b in ((1, 2), (2, 3), (3, 1)):
    link(P[a], P[b], 'varie')
for k, p in P.items():
    disc(ax, p[0], p[1], r, 'sujet', label=str(k), size='m')
text(ax, 20, 21, r'$(123)$', 'varie', 'l', weight='bold')
xs = [52, 64, 76]
text(ax, 64, 56, r'1. d’abord $(12)$', 'sujet', 's', weight='bold')
text(ax, 64, 36, r'2. ensuite $(13)$', 'autre', 's', weight='bold')
for k, x in enumerate(xs):
    disc(ax, x, 48, r, 'sujet', label=str(k + 1), size='m')
    disc(ax, x, 28, r, 'autre', label=str(k + 1), size='m')
link((xs[0], 48), (xs[1], 48), 'sujet', both=True)
link((xs[0], 28), (xs[2], 28), 'autre', both=True, curve=0.5)
arrow(ax, (84, 44), (84, 32), 'fixe', lw=1.2)
text(ax, 44, 8, r'$(123)$ = 2 échanges : pair', 'resultat', 's', weight='bold')
save(fig, '64-046')
