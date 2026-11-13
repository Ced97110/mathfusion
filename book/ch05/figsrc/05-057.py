import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
R = 4.2
def edge(p, q, role='fixe'):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    line(ax, [(p[0] + dx / d * R, p[1] + dy / d * R), (q[0] - dx / d * R, q[1] - dy / d * R)], role)
def node(p, v, prime):
    if prime: disc(ax, p[0], p[1], R, 'resultat', label=str(v))
    else: disc(ax, p[0], p[1], R, 'sujet', fill=False, label=str(v))
ys = [58, 44, 30, 16]
P = {'60': (20, ys[0]), '2a': (8, ys[1]), '30': (32, ys[1]), '2b': (22, ys[2]), '15': (42, ys[2]), '3': (34, ys[3]), '5': (50, ys[3])}
for a, b in [('60', '2a'), ('60', '30'), ('30', '2b'), ('30', '15'), ('15', '3'), ('15', '5')]:
    edge(P[a], P[b])
for k, v, pr in [('60', 60, 0), ('2a', 2, 1), ('30', 30, 0), ('2b', 2, 1), ('15', 15, 0), ('3', 3, 1), ('5', 5, 1)]:
    node(P[k], v, pr)
text(ax, 86, ys[1], r'$2 \times 30 = 60$', 'varie', 's', ha='right')
text(ax, 86, ys[2], r'$2 \times 2 \times 15 = 60$', 'varie', 's', ha='right')
text(ax, 86, ys[3], r'$2 \times 2 \times 3 \times 5 = 60$', 'varie', 's', ha='right')
disc(ax, 60, 60, 2.2, 'resultat'); text(ax, 63, 60, 's\'arrête', 'resultat', 's', ha='left')
disc(ax, 60, 54, 2.2, 'sujet', fill=False); text(ax, 63, 54, 'continue', 'sujet', 's', ha='left')
save(fig, '05-057')
