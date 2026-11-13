import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(58)
text(ax, 24, 54, 'Horloge à 12', 'sujet', 's')
text(ax, 68, 54, 'Horloge à 4', 'sujet', 's')
for cx, n, R, lab in [(24, 12, 17, {0: '0', 1: '1', 2: '2', 11: '11'}), (68, 4, 12, {0: '0', 1: '1', 2: '2', 3: '3'})]:
    P = ring(cx, 27, R, n)
    for k in range(n):
        disc(ax, P[k][0], P[k][1], 2.5, 'fixe' if k == 0 else 'resultat', label=lab.get(k), size='s')
        hop(ax, P[k], P[(k + 1) % n], 2.7, 'varie', 0.0, 0.8)
text(ax, 24, 27, '+1', 'varie', 'm')
text(ax, 68, 27, '+1', 'varie', 'm')
text(ax, 44, 4, 'toutes les heures visitées dans l’ordre', 'resultat', 's')
save(fig, '46-085')
