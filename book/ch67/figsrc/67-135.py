import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
box(ax, 22, 70, 44, 10, 'fixe', label='extension galoisienne')
arrow(ax, (34, 69.5), (22, 61), 'fixe')
arrow(ax, (54, 69.5), (66, 61), 'fixe')
box(ax, 2, 42, 40, 18, 'sujet', label='$G$ cyclique :\npreuve précédente\n(couvre les corps finis)', size='s')
box(ax, 46, 42, 40, 18, 'autre', label='$F$ infini :\nargument d’Artin\n(indépendance algébrique)', size='s')
# left : cyclic group of 3 elements drawn as a cycle
cx, cy, R = 22, 28, 7.5
pts = [(cx + R * math.cos(math.radians(90 + 120 * k)), cy + R * math.sin(math.radians(90 + 120 * k))) for k in range(3)]
for k in range(3):
    p, q = pts[k], pts[(k + 1) % 3]
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy)
    a = (p[0] + dx / d * 2.8, p[1] + dy / d * 2.8)
    b = (q[0] - dx / d * 2.8, q[1] - dy / d * 2.8)
    arrow(ax, a, b, 'sujet')
for p in pts:
    disc(ax, p[0], p[1], 2.2, 'sujet')
text(ax, 22, 14, r'$\mathbb{F}_8$ sur $\mathbb{F}_2$', 'sujet', 's')
text(ax, 22, 8, '3 éléments, cyclique', 'sujet', 's')
# right : group of 4 elements, no single generator
for (x, y) in [(60, 33), (70, 33), (60, 23), (70, 23)]:
    disc(ax, x, y, 2.2, 'autre')
text(ax, 65, 14, r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$ sur $\mathbb{Q}$', 'autre', 's')
text(ax, 65, 8, '4 éléments, pas cyclique', 'autre', 's')
save(fig, '67-135')
