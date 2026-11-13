import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(56)
text(ax, 22, 52, 'pas 4', 'sujet', 's')
text(ax, 66, 52, 'pas 5', 'autre', 's')
for cx, step, role, vis, name in [(22, 4, 'sujet', {0, 4, 8}, 'o(4) = 3'), (66, 5, 'autre', set(range(12)), 'o(5) = 12')]:
    P = ring(cx, 31, 15, 12)
    for k in range(12):
        disc(ax, P[k][0], P[k][1], 2.1, role if k in vis else 'fixe', label='0' if k == 0 else None, size='s')
    k = 0
    while True:
        hop(ax, P[k], P[(k + step) % 12], 2.3, 'varie', 0.0, 0.7)
        k = (k + step) % 12
        if k == 0: break
    text(ax, cx, 9, name, role, 's')
text(ax, 44, 3, 'ordre = pas du premier retour à 0', 'resultat', 's')
save(fig, '46-094')
