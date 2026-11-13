import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
cx, cy, R, r = 44, 30, 16, 4.5
names = ['i', 'j', 'k']
roles = ['sujet', 'autre', 'resultat']
angs = [90, -30, 210]
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in angs]
prods = [r'$i\times j=k$', r'$j\times k=i$', r'$k\times i=j$']
for n in range(3):
    p, q = pts[n], pts[(n + 1) % 3]
    d = math.hypot(q[0] - p[0], q[1] - p[1])
    ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * (r + 0.6), p[1] + uy * (r + 0.6))
    b = (q[0] - ux * (r + 0.6), q[1] - uy * (r + 0.6))
    main = (n == 2)
    arrow(ax, a, b, 'varie' if main else 'fixe', lw=1.8 if main else 1.0)
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    ox, oy = m[0] - cx, m[1] - cy
    nrm = math.hypot(ox, oy)
    text(ax, m[0] + ox / nrm * 13, m[1] + oy / nrm * 8, prods[n], 'varie' if main else 'encre', 's')
for n in range(3):
    disc(ax, pts[n][0], pts[n][1], r, roles[n], label=f'${names[n]}$', size='l')
text(ax, 44, 3, 'après $k$, on revient à $i$', 'encre', 's')
save(fig, '41-119')
