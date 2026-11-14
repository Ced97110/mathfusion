import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, r = 44, 33, 18
def P(h, rr=r):
    a = math.radians(90 - 30 * h)
    return (cx + rr * math.cos(a), cy + rr * math.sin(a))
text(ax, 44, 66, 'chaque flèche : + 3', 'varie', 'm')
for h in range(12):
    if h % 3 == 0:
        disc(ax, *P(h), 2, 'sujet')
    else:
        disc(ax, *P(h), 1.2, 'fixe')
for h in (0, 3, 6, 9):
    text(ax, *P(h, 23), str(h), 'sujet', 'm')
for k, h in enumerate((0, 3, 6, 9)):
    h2 = (h + 3) % 12
    p, q = P(h), P(h2)
    d = math.hypot(q[0] - p[0], q[1] - p[1])
    u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + 3 * u[0], p[1] + 3 * u[1]), (q[0] - 3 * u[0], q[1] - 3 * u[1]), 'varie', lw=1.2)
    mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    text(ax, cx + (mid[0] - cx) * 0.62, cy + (mid[1] - cy) * 0.62, str(k + 1), 'varie', 's')
text(ax, cx, cy, '|3| = 4', 'resultat', 'm')
save(fig, '60-088')
