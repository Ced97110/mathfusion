import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(46)
vals = ['1/8', '1/4', '1/2', '1', '2', '4', '8', '16']
x0, dx, y = 9, 10, 24
for i, v in enumerate(vals):
    x = x0 + i * dx
    box(ax, x - 4.2, y - 4, 8.4, 8, 'sujet' if i != 3 else 'resultat', label=v, size='s')
    if i < 7:
        hop(ax, (x + 4.2, y), (x + dx - 4.2, y), 0, 'varie', 0.0, 0.8)
text(ax, 3, y, '…', 'fixe', 'm')
text(ax, 85, y, '…', 'fixe', 'm')
text(ax, x0 + 3 * dx, 12, 'exposant 0', 'resultat', 's')
arrow(ax, (x0 + 3 * dx, 14.5), (x0 + 3 * dx, 19.5), 'resultat', lw=0.7)
text(ax, x0 + 5.5 * dx, 36, '× 2 à chaque pas', 'varie', 's')
text(ax, x0 + 1.5 * dx, 36, '÷ 2 à chaque pas', 'varie', 's')
text(ax, 44, 4, 'jamais deux fois la même valeur', 'sujet', 's')
save(fig, '46-088')
