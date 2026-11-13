import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def edge(a, b, r, role):
    dx, dy = b[0] - a[0], b[1] - a[1]; k = r / math.hypot(dx, dy)
    line(ax, [(a[0] + dx * k, a[1] + dy * k), (b[0] - dx * k, b[1] - dy * k)], role)
pos = {'1': (0, 0), '2': (-6, 14), '3': (6, 14), '4': (-6, 28), '6': (6, 28), '12': (0, 42)}
links = [('1', '2'), ('1', '3'), ('2', '4'), ('2', '6'), ('3', '6'), ('4', '12'), ('6', '12')]
role = {'4': 'sujet', '12': 'varie'}
for cx, base, flip, title in [(22, 10, 1, 'ce livre : diviseur en bas'), (66, 52, -1, 'Jacobson : diviseur en haut')]:
    text(ax, cx, 66, title, 'fixe', 's')
    P = {k: (cx + v[0], base + flip * v[1]) for k, v in pos.items()}
    for a, b in links: edge(P[a], P[b], 3.6, 'fixe')
    for k, p in P.items(): disc(ax, p[0], p[1], 3.6, role.get(k, 'fixe'), label=k, size='s')
save(fig, '79-026')
