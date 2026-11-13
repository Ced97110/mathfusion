import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(62)
text(ax, 22, 58, 'Horloge à 12 : 1 suffit', 'sujet', 's')
text(ax, 66, 58, 'S₃ : aucun seul ne suffit', 'autre', 's')
P = ring(22, 30, 17, 12)
for k in range(12):
    disc(ax, P[k][0], P[k][1], 2.4, 'fixe' if k == 0 else 'resultat', label={0: '0', 1: '1'}.get(k), size='s')
for k in range(12):
    hop(ax, P[k], P[(k + 1) % 12], 2.6, 'varie', 0.0, 0.7)
text(ax, 22, 30, '+1', 'varie', 'm')
Q = ring(66, 30, 13, 6)
for k, o in enumerate(['1', '2', '3', '2', '3', '2']):
    disc(ax, Q[k][0], Q[k][1], 4, 'autre', label=o, size='m')
text(ax, 66, 30, 'ordres', 'autre', 's')
text(ax, 22, 6, '1 donne les 12 heures', 'resultat', 's')
text(ax, 66, 6, 'jamais l\'ordre 6', 'limite', 's')
save(fig, '46-081')
