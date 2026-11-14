import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
text(ax, 44, 92, '5 pays voisins deux à deux', 'fixe', 's')
cx, cy, R = 44, 54, 26
P = [(cx + R * math.cos(math.radians(90 + 72 * i)), cy + R * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
import itertools
def cut(p, q, r=6):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)
for a, b in itertools.combinations(range(5), 2): line(ax, list(cut(P[a], P[b])), 'fixe')
for i, (x, y) in enumerate(P): disc(ax, x, y, 6, 'limite' if i == 4 else 'sujet', label=str(4 - i), size='l')
text(ax, 44, 20, 'choix de couleur par pays, k = 4', 'fixe', 's')
text(ax, 44, 9, r'$4\times3\times2\times1\times0=0$', 'limite', 'l')
save(fig, '80-384')
