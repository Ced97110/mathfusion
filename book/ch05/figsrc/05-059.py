import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
R = 3.9
def edge(p, q, role):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    line(ax, [(p[0] + dx / d * R, p[1] + dy / d * R), (q[0] - dx / d * R, q[1] - dy / d * R)], role)
def node(p, v, prime, role):
    if prime: disc(ax, p[0], p[1], R, 'resultat', label=str(v))
    else: disc(ax, p[0], p[1], R, role, fill=False, label=str(v))
ys = [58, 44, 30, 16]
root = (42, ys[0])
A = {'2a': (8, ys[1]), '30': (24, ys[1]), '2b': (16, ys[2]), '15': (32, ys[2]), '3': (25, ys[3]), '5': (39, ys[3])}
B = {'6': (62, ys[1]), '10': (80, ys[1]), '2c': (55, ys[2]), '3b': (69, ys[2]), '2d': (73, ys[2] - 14), '5b': (86, ys[2] - 14)}
# arbre B : 10 -> 2 et 5 ; positions ajustées
B = {'6': (56, ys[1]), '10': (77, ys[1]), '2c': (50, ys[2]), '3b': (62, ys[2]), '2d': (71, ys[2]), '5b': (83, ys[2])}
for a, b in [('30', '2a'), ('30', '30')]:
    pass
for a, b in [('2a', None)]:
    pass
edgesA = [('r', '2a'), ('r', '30'), ('30', '2b'), ('30', '15'), ('15', '3'), ('15', '5')]
PA = dict(A); PA['r'] = root
for a, b in edgesA: edge(PA[a], PA[b], 'sujet')
PB = dict(B); PB['r'] = root
for a, b in [('r', '6'), ('r', '10'), ('6', '2c'), ('6', '3b'), ('10', '2d'), ('10', '5b')]: edge(PB[a], PB[b], 'autre')
for k, v, pr in [('2a', 2, 1), ('30', 30, 0), ('2b', 2, 1), ('15', 15, 0), ('3', 3, 1), ('5', 5, 1)]:
    node(A[k], v, pr, 'sujet')
for k, v, pr in [('6', 6, 0), ('10', 10, 0), ('2c', 2, 1), ('3b', 3, 1), ('2d', 2, 1), ('5b', 5, 1)]:
    node(B[k], v, pr, 'autre')
disc(ax, 42, ys[0], R, 'fixe', label='60')
text(ax, 44, 4, 'mêmes premiers, autre ordre', 'resultat', 'm')
save(fig, '05-059')
