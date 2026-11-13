import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
r = 6.5
P = {'Léa': (18, 44), 'Hugo': (70, 44), 'Inès': (70, 14), 'élève 4': (18, 14)}
names = list(P)
def seg(p, q):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return [(p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)]
for a, b in itertools.combinations(names, 2):
    line(ax, seg(P[a], P[b]), 'sujet', lw=1.4)
for nm, (x, y) in P.items():
    disc(ax, x, y, r, 'fixe', label=nm, size='s')
text(ax, 44, 52, 'un secret', 'sujet', 's')
text(ax, 44, 4, '4 élèves → 6 secrets', 'encre')
save(fig, '53-003')
