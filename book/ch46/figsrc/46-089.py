import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(66)
text(ax, 44, 62, 'U(9) : ordre 6', 'sujet', 'm')
P = ring(44, 30, 20, 6)
seq = ['1', '2', '4', '8', '7', '5']
for k in range(6):
    disc(ax, P[k][0], P[k][1], 4.2, 'resultat' if k == 0 else 'sujet', label=seq[k], size='m')
    hop(ax, P[k], P[(k + 1) % 6], 4.4, 'varie', 0.0, 0.9)
Q = ring(44, 30, 27, 6)
for k in range(6):
    text(ax, Q[k][0], Q[k][1], r'$2^{%d}$' % k, 'fixe', 's')
text(ax, 44, 30, '×2, reste mod 9', 'varie', 's')
save(fig, '46-089')
