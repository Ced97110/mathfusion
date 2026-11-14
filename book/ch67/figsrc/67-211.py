import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sh(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)

fig, ax = canvas(80)
text(ax, 44, 74, r'$f_3=x\,(x^5+x^4-x+1)$', 'encre', 'm')
cx, cy, R = 58, 36, 18
pts = [(cx + R * math.cos(math.radians(90 + 72 * i)), cy + R * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
for i in range(5):
    a, b = sh(pts[i], pts[(i + 1) % 5], 4.4)
    arrow(ax, a, b, 'varie', lw=1.1)
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=rf'$r_{i + 2}$', size='s')
disc(ax, 14, 36, 3.6, 'fixe', label=r'$r_1$', size='s')
text(ax, 14, 47, 'degré 1', 'fixe', 's')
text(ax, 14, 27, 'racine fixée', 'fixe', 's')
text(ax, 58, 65, 'degré 5', 'sujet', 's')
text(ax, 58, 10, 'les cinq autres tournent', 'varie', 's')
save(fig, '67-211')
