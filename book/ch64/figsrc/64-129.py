import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
R = 3.6

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

# le sous-groupe normal N, avec sigma = (1 2 3) dedans
box(ax, 3, 6, 40, 38, 'sujet', fill=False, dash=True)
text(ax, 10, 39, r'$N$', 'sujet', 'l')
pts = [(23, 34), (14, 16), (32, 16)]
# ordre 1 -> 2 -> 3 : sens horaire
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], R, 'sujet', label=str(i + 1))
for i in range(3):
    p, q = pts[i], pts[(i + 1) % 3]
    arrow(ax, edge(p, q, R), edge(q, p, R), 'sujet')
text(ax, 23, 8.5, r'$\sigma=(1\,2\,3)$', 'sujet', 's')

# constat
arrow(ax, (45, 25), (55, 25), 'varie')
text(ax, 50, 30, 'constat', 'varie', 's')
box(ax, 57, 12, 28, 26, 'resultat', label='un 3-cycle\nest dans $N$')
save(fig, '64-129')
