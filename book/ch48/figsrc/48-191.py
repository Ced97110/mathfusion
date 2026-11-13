import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(88)
box(ax, 24, 72, 40, 12, 'sujet', label='groupe cyclique')
arrow(ax, (36, 71), (22, 58), 'fixe'); arrow(ax, (52, 71), (66, 58), 'fixe')
text(ax, 22, 54, 'ordre fini m', 'autre', 's', weight='bold'); text(ax, 66, 54, 'ordre infini', 'varie', 's', weight='bold')
C, R = (22, 34), 12
P = lambda k: (C[0] + R * math.cos(math.pi / 2 - 2 * math.pi * k / 15), C[1] + R * math.sin(math.pi / 2 - 2 * math.pi * k / 15))
for k in range(15):
    if k % 5: disc(ax, *P(k), 0.9, 'fixe')
for k in (0, 5, 10):
    disc(ax, *P(k), 3.2, 'autre', label=str(k), size='s')
for k in (0, 5, 10):
    p, q = P(k), P((k + 5) % 15)
    a = (p[0] + (q[0] - p[0]) * 0.3, p[1] + (q[1] - p[1]) * 0.3); b = (p[0] + (q[0] - p[0]) * 0.7, p[1] + (q[1] - p[1]) * 0.7)
    arrow(ax, a, b, 'autre', curve=-0.25)
text(ax, 22, 16, 'horloge à 15, élément 5', 'autre', 's'); text(ax, 22, 9, 'm = 3 pas : comme ℤ/mℤ', 'autre', 's')
for i, v in enumerate((0, 2, 4, 6)):
    disc(ax, 48 + i * 9, 34, 3.2, 'varie', label=str(v), size='s')
arrow(ax, (78, 34), (85, 34), 'varie')
text(ax, 66, 16, 'élément 2 dans ℤ', 'varie', 's'); text(ax, 66, 9, 'jamais 0 : comme ℤ', 'varie', 's')
save(fig, '48-191')
