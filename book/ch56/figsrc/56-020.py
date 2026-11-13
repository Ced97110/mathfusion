import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 58, 'horloge à 6 heures', 'encre', 's')
cx, cy, R = 22, 34, 14
pos = {}
for h in range(6):
    th = math.radians(90 - 60 * h)
    pos[h] = (cx + R * math.cos(th), cy + R * math.sin(th))
def edge(p, q, d0, d1):
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    return (p[0] + dx / n * d0, p[1] + dy / n * d0), (q[0] - dx / n * d1, q[1] - dy / n * d1)
for a in (1, 4):
    s, e = edge(pos[a], pos[2], 3.8, 4.2)
    arrow(ax, s, e, 'varie', curve=0.0)
for h in range(6):
    role = 'resultat' if h == 2 else ('sujet' if h in (1, 4) else 'fixe')
    disc(ax, pos[h][0], pos[h][1], 3.4, role, label=str(h), size='s')
text(ax, cx, cy, '×2', 'varie', 's')
text(ax, 22, 8, 'même résultat, 1 ≠ 4', 'limite', 's')
text(ax, 66, 58, 'dans ℤ', 'encre', 's')
box(ax, 50, 38, 34, 9, 'sujet', label='2 × 1 = 2')
box(ax, 50, 24, 34, 9, 'sujet', label='2 × 4 = 8')
text(ax, 66, 14, 'résultats différents', 'resultat', 's')
save(fig, '56-020')
