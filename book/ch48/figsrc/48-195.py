import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = (23, 34); h = 11
vs = {1: (c[0] - h, c[1] - h), 2: (c[0] + h, c[1] - h), 3: (c[0] + h, c[1] + h), 4: (c[0] - h, c[1] + h)}
poly(ax, list(vs.values()), 'sujet')
for k in range(1, 5):
    p, q = vs[k], vs[k % 4 + 1]
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    ox, oy = -dy / n * 6.5, dx / n * 6.5
    arrow(ax, (p[0] + dx / n * 5.5 - ox * 0, p[1] + dy / n * 5.5), (q[0] - dx / n * 5.5, q[1] - dy / n * 5.5), 'varie') if False else None
    arrow(ax, (p[0] + dx / n * 5 + ox, p[1] + dy / n * 5 + oy), (q[0] - dx / n * 5 + ox, q[1] - dy / n * 5 + oy), 'varie')
for k, (x, y) in vs.items():
    disc(ax, x, y, 3.4, 'sujet', label=str(k), size='m')
text(ax, 23, 8, 'rotation de 90°', 'varie', 'm')
text(ax, 67, 56, 'permutation des sommets', 'autre', 's')
tx = [52 + 9 * i for i in range(4)]
for i, x in enumerate(tx):
    disc(ax, x, 46, 3.4, 'sujet', label=str(i + 1), size='s')
    disc(ax, x, 18, 3.4, 'resultat', label=str(i + 1), size='s')
    j = (i + 1) % 4
    arrow(ax, (x, 42.2), (tx[j], 22.2), 'varie', lw=0.8)
text(ax, 67, 8, 'avant', 'sujet', 's', ha='center') if False else None
text(ax, 44, 3, 'chaque sommet reçoit un seul sommet', 'fixe', 's') if False else None
save(fig, '48-195')
