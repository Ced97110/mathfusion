import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(92)
R = 6.5
P = [(44, 78), (57, 55.5), (31, 55.5)]
labs = [r'$\alpha$', r'$\alpha^{2}$', r'$\alpha^{2}+\alpha$']
for (x, y), l in zip(P, labs):
    disc(ax, x, y, R, 'sujet', label=l, size='s')

def edge(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1])
    ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)

for i in range(3):
    a, b = edge(P[i], P[(i + 1) % 3], R)
    arrow(ax, a, b, 'varie')
text(ax, 44, 64, 'carré', 'varie', 's')
text(ax, 44, 38, r'$\alpha+\alpha^{2}+(\alpha^{2}+\alpha)$', 'sujet', 'm')
text(ax, 44, 30, r'$=2\alpha+2\alpha^{2}=0$ car $2=0$', 'sujet', 'm')
text(ax, 44, 21, r'trace $T(\alpha)=0$', 'resultat', 'm')
text(ax, 44, 11, 'liés : pas de base', 'limite', 'm')
save(fig, '67-191')
