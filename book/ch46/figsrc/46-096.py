import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(72)
box(ax, 10, 52, 68, 16, 'fixe')
text(ax, 44, 63, 'aucune puissance de a', 'encre', 's')
text(ax, 44, 57, 'ne revient au neutre', 'encre', 's')
arrow(ax, (44, 51.5), (44, 42), 'varie', lw=1.0)
parts = [(14, 'sujet', r'$o$'), (30, 'fixe', r'$(a)$'), (46, 'fixe', r'$=$'), (62, 'autre', r'$\infty$')]
for x, r, t in parts:
    box(ax, x, 28, 14, 12, r, label=t, size='xl')
text(ax, 21, 22, 'ordre', 'sujet', 's')
text(ax, 37, 22, 'élément', 'fixe', 's')
text(ax, 69, 22, 'jamais de retour', 'autre', 's')
text(ax, 44, 8, r'dans $\mathbb{Z}$ : $o(1) = \infty$', 'resultat', 'm')
save(fig, '46-096')
