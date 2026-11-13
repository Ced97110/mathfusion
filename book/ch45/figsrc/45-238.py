import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R, r = 44, 31, 21, 3.6
P = lambda k: (cx + R * math.cos(math.radians(90 - 30 * k)), cy + R * math.sin(math.radians(90 - 30 * k)))
def cut(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
for a, b in [(0, 8), (8, 4), (4, 0)]:
    p, q = cut(P(a), P(b), r + 0.3); arrow(ax, p, q, 'varie', lw=1.3)
for k in range(12):
    role = 'resultat' if k == 0 else ('sujet' if k in (8, 4) else 'fixe')
    disc(ax, *P(k), r, role, label=str(k), size='s')
text(ax, 44, 33, '3 pas de 8', 'varie', 'm', weight='bold')
text(ax, 44, 27, '8, 4, 0', 'varie', 'm')
save(fig, '45-238')
