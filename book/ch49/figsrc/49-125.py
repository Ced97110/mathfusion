import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 44, 38, 22
arrow(ax, (ox - u - 8, oy), (ox + u + 8, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - u - 8), (ox, oy + u + 8), 'fixe', lw=0.8)
P = {'a': (1, 0), 'b': (0, 1), 'c': (-1, 0)}
pt = {k: (ox + v[0] * u, oy + v[1] * u) for k, v in P.items()}
def short(p, q, d=2.6):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    return (p[0] + d * dx / n, p[1] + d * dy / n), (q[0] - d * dx / n, q[1] - d * dy / n)
for p, q in [('a', 'b'), ('b', 'c')]:
    s, e = short(pt[p], pt[q], 3.4)
    arrow(ax, s, e, 'varie', curve=0.3)
for k in 'abc':
    disc(ax, pt[k][0], pt[k][1], 2.2, 'sujet')
text(ax, pt['a'][0] + 1, pt['a'][1] - 5, '(1, 0)', 'sujet', 's', ha='left')
text(ax, pt['b'][0] + 4, pt['b'][1] + 4, '(0, 1)', 'sujet', 's', ha='left')
text(ax, pt['c'][0] - 1, pt['c'][1] - 5, '(−1, 0)', 'sujet', 's', ha='right')
text(ax, ox + 17, oy + 17, 'matrice', 'varie', 's')
text(ax, ox - 17, oy + 17, 'matrice', 'varie', 's')
text(ax, 44, 72, r'le plan $\mathbb{R}^2$ est déplacé', 'encre', 's')
text(ax, 44, 5, 'quart de tour', 'varie', 's')
save(fig, '49-125')
