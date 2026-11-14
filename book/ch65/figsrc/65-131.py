import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(92)
cx, cy, R = 30, 68, 15
P = [(cx + R * math.sin(2 * math.pi * k / 5), cy + R * math.cos(2 * math.pi * k / 5)) for k in range(5)]
for k in range(5):
    a, b = P[k], P[(k + 1) % 5]
    d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    arrow(ax, (a[0] + 3 * ux, a[1] + 3 * uy), (b[0] - 3 * ux, b[1] - 3 * uy), 'sujet')
for k, (x, y) in enumerate(P):
    disc(ax, x, y, 2.6, 'sujet', label=str(k + 1))
text(ax, 64, 76, 'cycle d\'ordre 5', 'sujet', 's')
text(ax, 64, 70, r'$1\to2\to3\to4\to5\to1$', 'sujet', 's')
text(ax, 64, 60, 'et un échange (1 2)', 'varie', 's')
# la chaîne des échanges de voisins
labs = ['(1 2)', '(2 3)', '(3 4)', '(4 5)']
for i, s in enumerate(labs):
    x = 3 + i * 21.5
    box(ax, x, 28, 17, 10, 'varie', label=s, size='s')
    if i < 3:
        arrow(ax, (x + 17.5, 33), (x + 21, 33), 'varie')
text(ax, 44, 44, 'le cycle décale chaque échange', 'varie', 's')
brace(ax, 3, 85, 26, 'resultat', label='4 échanges de voisins', down=True)
box(ax, 14, 3, 60, 10, 'resultat', label=r'$G=S_5$ : tout se fabrique')
save(fig, '65-131')
