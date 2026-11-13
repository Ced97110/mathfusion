import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R, r = 44, 40, 29, 4.2
pos = []
for k in range(12):
    a = math.radians(90 - 30 * k)
    pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for k in range(12):
    p, q = pos[k], pos[(k + 1) % 12]
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + ux * (r + 0.4), p[1] + uy * (r + 0.4)), (q[0] - ux * (r + 0.4), q[1] - uy * (r + 0.4)), 'varie', lw=0.9)
for k in range(12):
    disc(ax, pos[k][0], pos[k][1], r, 'sujet' if k == 1 else 'resultat', label=str(k), size='m')
text(ax, cx, cy, '$M$ : 12 éléments\n' + r'$x_1=1$, $n=1$' + '\npas : $+1$', 'encre', 's')
save(fig, '59-034')
