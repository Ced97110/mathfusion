import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
R = 3.4

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

def cyc(pts, labels, role):
    for p, l in zip(pts, labels):
        disc(ax, p[0], p[1], R, role, label=str(l))
    n = len(pts)
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        arrow(ax, edge(p, q, R), edge(q, p, R), role)

# haut : deux 3-cycles (1 2 3) et (4 5 6)
text(ax, 44, 99, r'$\sigma$ : deux 3-cycles', 'sujet', 'm')
cyc([(14, 90), (32, 90), (23, 76)], [1, 2, 3], 'sujet')
cyc([(56, 90), (74, 90), (65, 76)], [4, 5, 6], 'sujet')

# milieu : le cycle rho mêle les deux
arrow(ax, (44, 68), (44, 52), 'varie')
text(ax, 62, 60, r'$\rho=(1\,2\,4)$', 'varie', 'm')

# bas : cycle de 5 objets (1 4 2 6 3)
cx, cy, rr = 44, 28, 14
order = [1, 4, 2, 6, 3]
pts = [(cx + rr * math.cos(math.radians(90 - 72 * k)), cy + rr * math.sin(math.radians(90 - 72 * k))) for k in range(5)]
cyc(pts, order, 'resultat')
text(ax, 44, 4, 'cycle de 5 objets : cas 2', 'resultat', 'm')
save(fig, '64-131')
