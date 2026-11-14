import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
cx, cy, R = 24, 38, 14
labs = ['1', r'$g$', r'$g^2$', r'$g^3$']
P = [(cx + R * math.cos(math.pi / 2 - k * math.pi / 2), cy + R * math.sin(math.pi / 2 - k * math.pi / 2)) for k in range(4)]
for k in range(4):
    a, b = P[k], P[(k + 1) % 4]
    d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    arrow(ax, (a[0] + 3.4 * ux, a[1] + 3.4 * uy), (b[0] - 3.4 * ux, b[1] - 3.4 * uy), 'sujet')
for k, (x, y) in enumerate(P):
    role = 'varie' if k in (0, 2) else 'sujet'
    disc(ax, x, y, 3.0, role, label=labs[k])
text(ax, cx, 63, r"$p=5$ : cyclique d'ordre 4", 'sujet', 's')
text(ax, 66, 58, 'sous-groupes', 'encre', 's')
box(ax, 50, 42, 36, 12, 'fixe', label='1 élément\n' + r'$\{1\}$', size='s')
box(ax, 50, 27, 36, 12, 'varie', label='2 éléments\n' + r'$\{1,\ g^2\}$', size='s')
box(ax, 50, 12, 36, 12, 'sujet', label='4 éléments\n' + r'$\{1,\ g,\ g^2,\ g^3\}$', size='s')
text(ax, 24, 8, r'orange : $1$ et $g^2$', 'varie', 's')
save(fig, '65-148')
