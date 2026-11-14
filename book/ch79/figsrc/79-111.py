import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def seg(p, q, r=4.5):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return [(p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)]
def part(cx, nodes, role, title, note, missing=False):
    box(ax, cx - 20, 4, 40, 66, role, fill=False, dash=missing)
    text(ax, cx, 65, title, role, 's', weight='bold')
    P = {'12': (cx, 52), '4': (cx - 9, 38), '6': (cx + 9, 38), '2': (cx, 24)}
    for a, b in [('12', '4'), ('12', '6'), ('4', '2'), ('6', '2')]:
        line(ax, seg(P[a], P[b]), 'limite' if missing and '2' in (a, b) else 'fixe', dash=missing and '2' in (a, b))
    for k, p in P.items():
        if k in nodes: disc(ax, *p, 4.5, 'sujet', label=k)
        else: disc(ax, *p, 4.5, 'limite', fill=False, label=k)
    text(ax, cx, 11, note, role, 's')
part(22, ('12', '4', '6', '2'), 'resultat', '{2, 4, 6, 12}', 'PGCD(4, 6) = 2\nreste dans la partie')
part(66, ('12', '4', '6'), 'limite', '{4, 6, 12}', 'PGCD(4, 6) = 2\nsort de la partie', True)
save(fig, '79-111')
