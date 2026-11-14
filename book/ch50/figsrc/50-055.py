import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
CX, CY, R, r = 44.0, 35.0, 26.0, 3.4
pos = {h: (CX + R * math.sin(math.radians(30 * h)), CY + R * math.cos(math.radians(30 * h))) for h in range(12)}
members = (0, 4, 8)
def short(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
for a, b in ((0, 4), (4, 8), (8, 0)):
    p, q = short(pos[a], pos[b], r + 0.6)
    arrow(ax, p, q, 'varie', lw=1.1)
for h in range(12):
    disc(ax, *pos[h], r, 'sujet' if h in members else 'fixe', label=str(h), size='s')
text(ax, CX, CY, r'$\langle 4 \rangle = \{0, 4, 8\}$', 'sujet', 's')
text(ax, 3, 4, 'chaque flèche : ajouter 4', 'varie', 's', ha='left')
save(fig, '50-055')
