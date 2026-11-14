import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cut(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return [(p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)]
fig, ax = canvas(80)
P = {1: (44, 10), 2: (30, 30), 3: (58, 30), 4: (30, 50), 6: (58, 50), 12: (44, 70)}
for p, q in ((1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)):
    line(ax, cut(P[p], P[q], 4.2), 'fixe')
role = {1: 'fixe', 3: 'fixe', 4: 'sujet', 6: 'sujet', 2: 'resultat', 12: 'resultat'}
for k, (x, y) in P.items(): disc(ax, x, y, 4.2, role[k], label=str(k))
text(ax, 25, 30, 'PGCD', 'resultat', 's', ha='right'); text(ax, 51, 70, 'PPCM', 'resultat', 's', ha='left')
text(ax, 25, 50, '4 et 6', 'sujet', 's', ha='right')
text(ax, 22, 8, 'diviseurs de 12', 'fixe', 's', ha='center')
save(fig, '80-466')
