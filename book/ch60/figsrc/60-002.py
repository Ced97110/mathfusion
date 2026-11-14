import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
R, rd = 15, 2.7
def pos(c, h):
    a = math.radians(90 - 30 * h)
    return (c[0] + R * math.cos(a), c[1] + R * math.sin(a))
def seg(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)
for c, step, visited, role in (((22, 29), 5, set((5 * k) % 12 for k in range(12)), 'resultat'), ((66, 29), 3, set((3 * k) % 12 for k in range(4)), 'sujet')):
    for k in range(12 if step == 5 else 4):
        a, b = seg(pos(c, (step * k) % 12), pos(c, (step * (k + 1)) % 12), rd + 0.3)
        arrow(ax, a, b, 'varie', lw=0.45 if step == 5 else 0.9)
    for h in range(12):
        x, y = pos(c, h)
        disc(ax, x, y, rd, role if h in visited else 'fixe', label='0' if h == 0 else None, size='s')
text(ax, 22, 8, 'ajouter 5 : 12 heures', 'resultat', 's')
text(ax, 66, 8, 'ajouter 3 : 4 heures', 'fixe', 's')
text(ax, 22, 2.5, 'cyclique : 5 les engendre toutes', 'resultat', 's', weight='bold')
text(ax, 66, 2.5, 'pas toutes', 'fixe', 's')
save(fig, '60-002')
