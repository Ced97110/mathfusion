import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(58)
vals = ['0', '4', '8', '0', '4']
for i, v in enumerate(vals):
    x = 8 + i * 16
    role = 'varie' if i in (1, 4) else 'fixe'
    box(ax, x, 28, 12, 9, role, label=v, size='m')
    text(ax, x + 6, 24, 'pas %d' % i, 'fixe', 's')
    if i < 4: arrow(ax, (x + 12.3, 32.5), (x + 15.7, 32.5), 'fixe', lw=0.8)
arrow(ax, (30, 38.5), (78, 38.5), 'varie', curve=-0.25, both=True)
text(ax, 54, 51, 'même heure : 4', 'varie', 's')
brace(ax, 30, 78, 21, 'varie', label='écart : 3 pas', depth=1.8)
box(ax, 22, 2, 44, 8, 'resultat', label=r'$3 \times 4 = 12 = 0$', size='m')
save(fig, '46-093')
