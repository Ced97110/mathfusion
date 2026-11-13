import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
P = {1: (28, 58), 2: (60, 58), 3: (28, 28), 4: (60, 28)}
import itertools
def cut(p, q, r=4.5):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)
for a, b in itertools.combinations(P, 2): line(ax, list(cut(P[a], P[b])), 'sujet', lw=1.3)
for k, (x, y) in P.items(): disc(ax, x, y, 4.5, 'sujet', label=str(k), size='l')
text(ax, 44, 79, 'un trait = un groupe de 2', 'fixe', 's')
text(ax, 44, 14, r'6 groupes : $24\div(2\times2)=6$', 'resultat', 'm')
save(fig, '80-375')
