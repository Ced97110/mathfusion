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
ys = [50, 38, 26, 14]
P = {'60': (18, ys[0]), '2a': (7, ys[1]), '30': (29, ys[1]), '2b': (19, ys[2]), '15': (39, ys[2]), '3': (31, ys[3]), '5': (47, ys[3])}
for a, b in [('60', '2a'), ('60', '30'), ('30', '2b'), ('30', '15'), ('15', '3'), ('15', '5')]:
    edge(P[a], P[b])
for k, v, pr in [('60', 60, 0), ('2a', 2, 1), ('30', 30, 0), ('2b', 2, 1), ('15', 15, 0), ('3', 3, 1), ('5', 5, 1)]:
    node(P[k], v, pr)
box(ax, 2, 4, 52, 54, 'sujet', fill=False, dash=True, lw=0.6, r=2)
text(ax, 28, 61, "l'arbre : le dessin", 'sujet', 's')
for k, v in enumerate([2, 2, 3, 5]):
    disc(ax, 74, 50 - k * 11, R, 'resultat', label=str(v))
box(ax, 66, 4, 16, 54, 'resultat', fill=False, dash=True, lw=0.6, r=2)
text(ax, 74, 61, 'la liste', 'resultat', 's')
arrow(ax, (56, 31), (64, 31), 'varie')
text(ax, 60, 25.5, 'ronds', 'varie', 's'); text(ax, 60, 22, 'verts', 'varie', 's')
save(fig, '05-058')
