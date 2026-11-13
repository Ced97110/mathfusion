import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
cx, cy, u = 22, 40, 4.0
text(ax, 4, 79, r'$f(x,\,y)=x^2+y^2$', 'encre', 'l', ha='left')
disc(ax, cx, cy, 5 * u, 'sujet', fill=False, lw=1.3)
disc(ax, cx, cy, 3 * u, 'autre', fill=False, lw=1.3)
text(ax, cx, cy + 5 * u + 3, r'$r=5$', 'sujet', 's')
text(ax, cx, cy + 3 * u + 2.8, r'$r=3$', 'autre', 's')
yt = lambda t: 8 + t * 2.4
tx = 64
arrow(ax, (tx, 6), (tx, 74), 'fixe', lw=0.9)
for t, role in [(0, 'fixe'), (9, 'autre'), (25, 'sujet')]:
    line(ax, [(tx - 1.5, yt(t)), (tx + 1.5, yt(t))], role)
    text(ax, tx + 3, yt(t), str(t), role, 'm', ha='left')
text(ax, tx, 77, r'$t$', 'fixe', 'm')
P = (cx + 3 * u, cy + 4 * u)
a = (cx + 3 * u * math.cos(math.radians(-30)), cy + 3 * u * math.sin(math.radians(-30)))
disc(ax, *P, 1.3, 'sujet'); disc(ax, *a, 1.3, 'autre')
arrow(ax, (P[0] + 2, P[1] + 1), (tx - 3, yt(25)), 'sujet')
arrow(ax, (a[0] + 2, a[1]), (tx - 3, yt(9)), 'autre')
text(ax, 30, 4, 'un cercle, un seul nombre', 'resultat', 's')
save(fig, '43-128')
