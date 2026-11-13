import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(56)
f = numberline(ax, 9, 79, 28, -5, 5, arrow_right=False, size='s')
for v in range(0, 5):
    arrow(ax, (f(v) + 0.5, 30), (f(v + 1) - 0.5, 30), 'varie', lw=0.9, curve=-0.5)
for v in range(0, -3, -1):
    arrow(ax, (f(v) - 0.5, 30), (f(v - 1) + 0.5, 30), 'autre', lw=0.9, curve=0.5)
text(ax, f(2.5), 38, r'$5 = 1+1+1+1+1$', 'varie', 's')
text(ax, f(-1.5), 38, r'$-3 = -(1+1+1)$', 'autre', 's')
disc(ax, f(0), 28, 1.2, 'resultat')
text(ax, f(0), 50, '0 : on n’ajoute rien', 'resultat', 's')
arrow(ax, (f(0), 48), (f(0), 31.5), 'resultat', lw=0.7)
text(ax, 44, 3, r'$\mathbb{Z}$ = tous les entiers atteints', 'sujet', 's')
save(fig, '46-084')
