import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'M = ℤ/12 : module sur ℤ', 'sujet', 'm')
cx, cy, r = 24, 30, 15
def P(h, rr=r):
    a = math.radians(90 - 30 * h)
    return (cx + rr * math.cos(a), cy + rr * math.sin(a))
for h in range(12):
    disc(ax, *P(h), 2.2 if h == 1 else 1.6, 'sujet' if h == 1 else 'resultat')
for h in (0, 1, 5):
    text(ax, *P(h, 20), str(h), 'sujet' if h == 1 else 'resultat', 'm')
p, q = P(1), P(5)
dx, dy = q[0] - p[0], q[1] - p[1]
n = math.hypot(dx, dy)
arrow(ax, (p[0] + dx / n * 3, p[1] + dy / n * 3), (q[0] - dx / n * 3, q[1] - dy / n * 3), 'varie')
text(ax, 32, 28, '× 5', 'varie', 'm')
text(ax, 50, 44, 'un seul élément : 1', 'sujet', 's', ha='left')
text(ax, 50, 36, '5 × 1 = 5', 'varie', 's', ha='left')
text(ax, 50, 28, 'chaque heure = k × 1 :', 'resultat', 's', ha='left')
text(ax, 50, 23, 'tout M est atteint', 'resultat', 's', ha='left')
save(fig, '60-074')
