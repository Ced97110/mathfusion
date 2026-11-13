import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, r = 24, 38, 17
P = {k: (cx + r * math.sin(math.radians(90 * k)), cy + r * math.cos(math.radians(90 * k))) for k in range(4)}
roles = {0: 'fixe', 1: 'sujet', 2: 'resultat', 3: 'autre'}
for k in range(4): disc(ax, *P[k], 4, roles[k], label=str(k), size='m')
def go(a, b, off, cv):
    p, q = P[a], P[b]; d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + ux * 4.6, p[1] + uy * 4.6), (q[0] - ux * 4.6, q[1] - uy * 4.6), 'varie', curve=cv)
go(1, 2, 0, 0.0); go(3, 2, 0, 0.0)
text(ax, cx + 11.5, cy - 11.5, r'$\times 2$', 'varie', 's'); text(ax, cx - 11.5, cy - 11.5, r'$\times 2$', 'varie', 's')
text(ax, cx, 10, 'Cadran à 4 heures', 'fixe', 's')
box(ax, 50, 42, 34, 22, 'resultat')
text(ax, 67, 58, r'$2 \times 1 = 2$', 'resultat', 'm')
text(ax, 67, 51.5, r'$2 \times 3 = 6 = 2$', 'resultat', 'm')
text(ax, 67, 45.5, 'mêmes produits', 'resultat', 's')
box(ax, 50, 12, 34, 22, 'limite')
text(ax, 67, 28, r'$1 \neq 3$', 'limite', 'l')
text(ax, 67, 21, 'simplifier par 2', 'limite', 's')
text(ax, 67, 16, 'est faux', 'limite', 's')
save(fig, '51-108')
