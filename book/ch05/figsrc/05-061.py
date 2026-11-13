import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
R = 4.2
def edge(p, q, role='varie'):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    line(ax, [(p[0] + dx / d * R, p[1] + dy / d * R), (q[0] - dx / d * R, q[1] - dy / d * R)], role)
def node(p, v, prime):
    if prime: disc(ax, p[0], p[1], R, 'resultat', label=str(v))
    else: disc(ax, p[0], p[1], R, 'sujet', fill=False, label=str(v))
ys = [60, 40, 20]
r0 = (62, ys[0]); n1 = (50, ys[1]); n2 = (74, ys[1])
leaves = [(44, 'a'), (56, 'b'), (68, 'c'), (80, 'd')]
for p, c in [(n1, leaves[0]), (n1, leaves[1]), (n2, leaves[2]), (n2, leaves[3])]:
    edge(p, (c[0], ys[2]))
edge(r0, n1); edge(r0, n2)
node(r0, 60, 0); node(n1, 6, 0); node(n2, 10, 0)
for (x, _), v in zip(leaves, [2, 3, 2, 5]): node((x, ys[2]), v, 1)
text(ax, 2, ys[0], r'départ : $n > 1$', 'sujet', 's', ha='left')
text(ax, 2, 50, r'$n = n_1 \times n_2$', 'varie', 's', ha='left')
text(ax, 2, 46, r'$n_1 < n$ et $n_2 < n$', 'varie', 's', ha='left')
text(ax, 2, ys[1], 'on recommence', 'varie', 's', ha='left')
text(ax, 2, ys[2], 'arrivée : premiers', 'resultat', 's', ha='left')
text(ax, 28.5, 40, 'les nombres diminuent', 'fixe', 's', rot=90)
arrow(ax, (33, 62), (33, 18), 'fixe', lw=0.8)
save(fig, '05-061')
