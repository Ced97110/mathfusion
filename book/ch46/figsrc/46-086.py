import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(56)
text(ax, 22, 52, 'ajouter 1 : sens croissant', 'varie', 's')
text(ax, 66, 52, 'ajouter 5 : sens inverse', 'autre', 's')
for cx, step, role in [(22, 1, 'varie'), (66, 5, 'autre')]:
    P = ring(cx, 27, 14, 6)
    for k in range(6):
        disc(ax, P[k][0], P[k][1], 3.2, 'fixe' if k == 0 else 'resultat', label=str(k), size='s')
    for k in range(6):
        hop(ax, P[k], P[(k + step) % 6], 3.4, role, 0.0, 0.8)
text(ax, 44, 4, 'Les deux visitent les 6 heures', 'resultat', 's')
save(fig, '46-086')
