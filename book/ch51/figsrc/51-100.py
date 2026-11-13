import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cx, cy, r = 25, 42, 22
P = {k: (cx + r * math.sin(math.radians(30 * k)), cy + r * math.cos(math.radians(30 * k))) for k in range(12)}
for k in range(12):
    disc(ax, *P[k], 3.3, 'sujet' if k % 3 == 0 else 'fixe', label=str(k), size='s')
# quatre bonds de 3 heures : 0 -> 3 -> 6 -> 9 -> 12 = 0
for a, b in [(0, 3), (3, 6), (6, 9), (9, 12)]:
    p, q = P[a % 12], P[b % 12]
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + ux * 3.8, p[1] + uy * 3.8), (q[0] - ux * 3.8, q[1] - uy * 3.8), 'varie', curve=-0.0)
text(ax, cx, cy + 3, '4 bonds', 'varie', 's'); text(ax, cx, cy - 3, 'de 3 heures', 'varie', 's')
text(ax, cx + 12, 71, r'$12 = 0$', 'sujet', 's')
text(ax, cx, 8, 'Cadran à 12 heures', 'fixe', 's')
text(ax, 67, 62, r'$3 \neq 0$', 'sujet', 'm')
text(ax, 67, 54, r'$4 \neq 0$', 'autre', 'm')
text(ax, 67, 44, r'$3 \times 4$', 'encre', 'l')
text(ax, 67, 36, r'$= 12 = 0$', 'varie', 'l')
text(ax, 67, 28, 'produit nul', 'varie', 's')
save(fig, '51-100')
