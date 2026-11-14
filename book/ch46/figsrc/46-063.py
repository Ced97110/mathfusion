import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(h, cx, cy, R):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))
def edge(p, q, off):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * off, p[1] + u[1] * off), (q[0] - u[0] * off, q[1] - u[1] * off)

fig, ax = canvas(80)
cx, cy, R = 44, 44, 22
for h in range(12):
    role = 'resultat' if h in (0, 4, 8) else ('limite' if h == 1 else 'fixe')
    disc(ax, *pos(h, cx, cy, R), 3.0, role, label=str(h), size='s')
P = {h: pos(h, cx, cy, R) for h in (0, 4, 8)}
for p, q in ((0, 4), (4, 8), (8, 0)):
    a, b = edge(P[p], P[q], 4.2); arrow(ax, a, b, 'varie', both=True)
text(ax, cx, cy, '± 4', 'varie', 'm')
text(ax, 44, 12, '0, 4, 8 : calculables à partir de 4', 'resultat', 's')
text(ax, 44, 5, '1 : impossible à calculer', 'limite', 's')
save(fig, '46-063')
