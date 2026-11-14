import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(52)
xs = [11, 33, 55, 77]
spec = [('1', 'resultat', range(6)), ('5', 'resultat', range(6)), ('2', 'limite', [0, 2, 4]), ('0', 'limite', [0])]
for x, (name, role, vis) in zip(xs, spec):
    box(ax, x - 10.5, 6, 21, 30, role, fill=False, lw=1.0)
    P = ring(x, 21, 6.5, 6)
    for k in range(6):
        disc(ax, P[k][0], P[k][1], 1.6, 'sujet' if k in vis else 'fixe')
    text(ax, x, 11, r'$\langle %s\rangle$' % name, role, 'm')
text(ax, 22, 44, 'engendre tout', 'resultat', 'm')
text(ax, 66, 44, 'n\'engendre pas tout', 'limite', 'm')
text(ax, 22, 40, r'$\langle a\rangle = G$', 'resultat', 's')
text(ax, 66, 40, r'$\langle a\rangle \neq G$', 'limite', 's')
save(fig, '46-082')
