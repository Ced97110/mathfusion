import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R, r = 24, 30, 21, 3.4
def P(k): a = math.radians(90 - 360 * k / 7); return (cx + R * math.cos(a), cy + R * math.sin(a))
def trim(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
seq = [0, 3, 6, 2, 5, 1, 4, 0]
for a, b in zip(seq, seq[1:]):
    p, q = trim(P(a), P(b), r + 0.4); arrow(ax, p, q, 'varie', lw=0.8, curve=0.12)
for k in range(7):
    x, y = P(k); disc(ax, x, y, r, 'fixe' if k else 'sujet', label=str(k))
text(ax, 68, 48, 'avancer de 3 :', 'varie', 's')
text(ax, 68, 42, '3, 6, 2, 5, 1, 4, 0', 'varie', 's')
text(ax, 68, 31, 'avancer de 5 :', 'autre', 's')
text(ax, 68, 25, '5, 3, 1, 6, 4, 2, 0', 'autre', 's')
text(ax, 68, 12, 'les 7 heures', 'resultat', 'm')
text(ax, 68, 6, 'dans les deux cas', 'resultat', 's')
save(fig, '46-264')
