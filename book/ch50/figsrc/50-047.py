import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
P = lambda c, a, r: (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
cl, cr = (22, 40), (66, 40)
for c in (cl, cr):
    poly(ax, [P(c, a, 14) for a in (90, 210, 330)], 'fixe')
for a in (90, 210, 330):
    line(ax, [P(cl, a, 19), P(cl, a + 180, 8)], 'sujet', lw=1.5)
for a in (10, 130, 250):
    pts = [P(cr, a + 95 * i / 30, 19) for i in range(31)]
    line(ax, pts, 'autre', lw=1.3)
    arrow(ax, pts[-3], pts[-1], 'autre', lw=1.3)
text(ax, 22, 16, r'$n_2=3$', 'sujet', 'l')
text(ax, 22, 9, '3 sous-groupes de 2 éléments', 'sujet', 's')
text(ax, 66, 16, r'$n_3=1$', 'autre', 'l')
text(ax, 66, 9, '1 sous-groupe de 3 éléments', 'autre', 's')
save(fig, '50-047')
