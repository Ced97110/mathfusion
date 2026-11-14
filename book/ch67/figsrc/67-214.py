import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sh(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)

fig, ax = canvas(92)
c = (44, 56); R = 26; rd = 3.8
ring = [(c[0] + R * math.cos(math.radians(90 + 72 * i)), c[1] + R * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
for i in range(5):
    a, b = sh(ring[i], ring[(i + 1) % 5], rd + 0.8)
    arrow(ax, a, b, 'fixe', lw=0.8, curve=0.25)
for i in range(1, 5):
    a, b = sh(c, ring[i], rd + 0.6)
    line(ax, [a, b], 'resultat', lw=1.1)
a, b = sh(c, ring[0], rd + 0.6)
arrow(ax, a, b, 'varie', lw=1.4, both=True)
disc(ax, c[0], c[1], rd, 'fixe', label=r'$r_1$', size='s')
disc(ax, ring[0][0], ring[0][1], rd, 'varie', label=r'$r_k$', size='s')
for i in range(1, 5):
    disc(ax, ring[i][0], ring[i][1], rd, 'sujet', label=r'$r_j$', size='s')
text(ax, 48, 68, r'$(r_1\,r_k)$', 'varie', 's', ha='left')
text(ax, 4, 86, 'le 5-cycle tourne', 'fixe', 's', ha='left')
text(ax, 44, 22, r'$(r_1\,r_j)$ pour tout $j$', 'resultat', 'm')
text(ax, 44, 13, r'ils engendrent $S_6$', 'resultat', 'm')
save(fig, '67-214')
