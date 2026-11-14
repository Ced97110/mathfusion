import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
c = (24, 30); R = 17
P = {k: (c[0] + R * math.cos(math.radians(a)), c[1] + R * math.sin(math.radians(a))) for k, a in {1: 90, 2: -30, 3: 210}.items()}
for k, (x, y) in P.items():
    disc(ax, x, y, 4.2, 'sujet', label=f'$r_{k}$', size='m')
def seg(a, b, d=5.4):
    p, q = P[a], P[b]; L = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
    return (p[0] + ux * d, p[1] + uy * d), (q[0] - ux * d, q[1] - uy * d)
for a, b in ((1, 2), (2, 3), (3, 1)):
    p, q = seg(a, b); arrow(ax, p, q, 'varie', curve=0.25)
text(ax, 68, 52, r'$(r_1\ r_2\ r_3)$', 'sujet', 'l')
text(ax, 68, 41, '=', 'varie', 'xl')
text(ax, 68, 30, r'$(r_2\ r_3\ r_1)$', 'sujet', 'l')
text(ax, 68, 17, 'même circuit,\ndépart différent', 'varie', 's')
save(fig, '65-030')
