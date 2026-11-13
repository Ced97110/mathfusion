import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 4.8
def panel(ox, order, num, role, sens):
    P = lambda x, y: (ox + u * x, 13 + u * y)
    pts = {'A': (1, 1), 'B': (7, 1), 'C': (6, 5)}
    poly(ax, [P(*pts[k]) for k in 'ABC'], 'sujet')
    for a, b in zip(order, order[1:] + order[:1]):
        p, q = P(*pts[a]), P(*pts[b]); d = (q[0] - p[0], q[1] - p[1])
        arrow(ax, (p[0] + .22 * d[0], p[1] + .22 * d[1]), (p[0] + .78 * d[0], p[1] + .78 * d[1]), 'varie', lw=1.3)
    for k, (dx, dy) in {'A': (-2.5, -2.8), 'B': (2.5, -2.8), 'C': (2.2, 2.4)}.items():
        text(ax, P(*pts[k])[0] + dx, P(*pts[k])[1] + dy, k, 'sujet', weight='bold')
    text(ax, ox + 3.5 * u, 41, num, role, 'xl', weight='bold')
    text(ax, ox + 3.5 * u, 5, sens, 'fixe', 's')
panel(3, 'ABC', '+24', 'resultat', 'sens inverse des aiguilles')
panel(47, 'ACB', r'$-24$', 'varie', 'sens des aiguilles')
text(ax, 44, 50, r'aire $= \frac{1}{2}\times|\pm 24| = 12$', 'encre', 's')
save(fig, '37-106')
