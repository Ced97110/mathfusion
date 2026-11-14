import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(78)
text(ax, 22, 72, r'$f$ modulo $\ell$', 'sujet', 's')
box(ax, 3, 52, 14, 12, 'varie', label='2', size='m')
box(ax, 19, 52, 21, 12, 'sujet', label='3', size='m')
text(ax, 10, 46, 'facteur', 'varie', 's')
text(ax, 30, 46, 'facteur', 'sujet', 's')
text(ax, 22, 40, 'degrés : 2 + 3 = 5', 'encre', 's')
arrow(ax, (44, 58), (52, 58), 'resultat', lw=1.4)
text(ax, 66, 72, 'cycles de ' + r'$G_f$', 'resultat', 's')
# deux disques liés, trois disques liés en cycle
a, b = (58, 56), (70, 56)
arrow(ax, (a[0] + 2.5, a[1] + 1.5), (b[0] - 2.5, b[1] + 1.5), 'varie', curve=0.0)
arrow(ax, (b[0] - 2.5, b[1] - 1.5), (a[0] + 2.5, a[1] - 1.5), 'varie')
disc(ax, a[0], a[1], 2.2, 'varie'); disc(ax, b[0], b[1], 2.2, 'varie')
c = [(56 + 0, 22), (76, 22), (66, 36)]
for i in range(3):
    p, q = c[i], c[(i + 1) % 3]
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2.8 * ux, p[1] + 2.8 * uy), (q[0] - 2.8 * ux, q[1] - 2.8 * uy), 'sujet')
for x, y in c:
    disc(ax, x, y, 2.2, 'sujet')
text(ax, 66, 12, 'un cycle de 2, un de 3', 'resultat', 's')
save(fig, '65-149')
