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
fig, ax = canvas(80)
phi = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4]
for q in range(1, 13):
    x = 9 + 6.3*(q-1); div = 12 % q == 0
    box(ax, x-2.3, 22, 4.6, phi[q-1]*3.2, 'resultat' if div else 'limite', r=0.3, lw=0.6)
    text(ax, x, 18, str(q), 'resultat' if div else 'limite', 's')
text(ax, 44, 73, 'diviseurs de 12 : somme 12', 'resultat', 'm')
text(ax, 44, 65, 'les autres ajoutent 34 : 46', 'limite', 'm')
save(fig, '46-255')
