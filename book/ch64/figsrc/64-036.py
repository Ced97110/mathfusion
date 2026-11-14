import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
r = 3.4; s = 9
def verts(cx, cy):
    return {1: (cx - s, cy - s), 2: (cx + s, cy - s), 3: (cx + s, cy + s), 4: (cx - s, cy + s)}
def link(p, q, role):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * (r + 0.5), p[1] + u[1] * (r + 0.5)), (q[0] - u[0] * (r + 0.5), q[1] - u[1] * (r + 0.5)), role, both=True)
for cx, pairs, role in [(17, [(1, 2), (3, 4)], 'sujet'), (71, [(2, 3), (1, 4)], 'limite')]:
    v = verts(cx, 34)
    line(ax, [v[1], v[2], v[3], v[4], v[1]], 'fixe', lw=0.5)
    for a, b in pairs:
        link(v[a], v[b], role)
    for k in v:
        disc(ax, v[k][0], v[k][1], r, 'sujet', label=str(k), size='m')
text(ax, 17, 17, r'$(12)(34)\ \in\ W$', 'resultat', 'm')
text(ax, 71, 17, r'$(14)(23)\ \notin\ W$', 'limite', 'm')
arrow(ax, (31, 34), (57, 34), 'varie')
text(ax, 44, 38.5, r'conjugué par $\rho$', 'varie', 's')
text(ax, 44, 29.5, r'$\rho=(1234)$', 'fixe', 's')
save(fig, '64-036')
