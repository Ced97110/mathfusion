import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
import math
c = (30, 34); R = 20
ang = {1: 90, 2: 210, 3: 330}   # r1 -> r2 -> r3 -> r1 dans le sens trigonométrique
P = {k: (c[0] + R * math.cos(math.radians(a)), c[1] + R * math.sin(math.radians(a))) for k, a in ang.items()}
for k, (x, y) in P.items():
    disc(ax, x, y, 4.2, 'sujet', label=f'$r_{k}$', size='m')
def shrink(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
    return (p[0] + ux * d, p[1] + uy * d), (q[0] - ux * d, q[1] - uy * d)
# le circuit : présent (orange)
for a, b in ((1, 2), (2, 3), (3, 1)):
    p, q = shrink(P[a], P[b], 5.3)
    arrow(ax, p, q, 'varie', curve=-0.3)
# l'échange r1 <-> r2 en laissant r3 : absent (rouge)
p, q = shrink(P[1], P[2], 5.3)
arrow(ax, p, q, 'limite', both=True)
line(ax, [(P[3][0], P[3][1] + 7), (P[3][0], P[3][1] + 7)], 'fixe')
mx, my = (P[1][0] + P[2][0]) / 2, (P[1][1] + P[2][1]) / 2
text(ax, mx, my, '×', 'limite', 'xl', weight='bold')
text(ax, 62, 56, 'présent :', 'varie', 's', ha='left')
text(ax, 62, 50, 'circuit', 'varie', 's', ha='left')
text(ax, 62, 36, 'absent :', 'limite', 's', ha='left')
text(ax, 62, 30, 'échange de $r_1$ et $r_2$,', 'limite', 's', ha='left')
text(ax, 62, 24, '$r_3$ reste en place', 'limite', 's', ha='left')
save(fig, '65-013')
