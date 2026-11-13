import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def sh(p, q, r):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    return (p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)
def ring(ax, cx, cy, R, labels, role, r=2.6, curve=-0.3, arrows=True, size='s'):
    n = len(labels); pts = []
    for i in range(n):
        a = math.pi/2 - 2*math.pi*i/n
        pts.append((cx + R*math.cos(a), cy + R*math.sin(a)))
    if arrows:
        for i in range(n):
            p, q = sh(pts[i], pts[(i+1) % n], r + 0.4)
            arrow(ax, p, q, role, lw=0.9, curve=curve)
    for p, l in zip(pts, labels):
        disc(ax, p[0], p[1], r, role, label=l, size=size)
    return pts
fig, ax = canvas(100)
text(ax, 44, 94, '12 racines', 'encre', 'm')
sizes = [1, 1, 2, 2, 2, 4]; xs = []; x = 6.8
for gi, s in enumerate(sizes):
    g = []
    for k in range(s): g.append(x); x += 5.4
    xs.append(g); x += 3 - 5.4 + 5.4
flat = [p for g in xs for p in g]
for i in range(12):
    t = (8 + 6.5*i, 84); b = (flat[i], 58)
    disc(ax, t[0], t[1], 2.4, 'fixe'); disc(ax, b[0], b[1], 2.4, 'resultat')
    p, q = sh(t, b, 2.8); arrow(ax, p, q, 'fixe', lw=0.6)
for g, s in zip(xs, sizes):
    q = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6, 6: 12}
for g, q in zip(xs, (1, 2, 3, 4, 6, 12)):
    text(ax, (g[0] + g[-1])/2, 50, str(q), 'resultat', 's')
text(ax, 44, 43, 'ordre de chaque groupe', 'fixe', 's')
text(ax, 44, 35, 'chaque racine : un seul groupe', 'encre', 's')
text(ax, 44, 25, r'$1+1+2+2+2+4=12$', 'resultat', 'l', weight='bold')
save(fig, '46-254')
