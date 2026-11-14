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
text(ax, 44, 74, 'nombre de racines d’ordre $q$', 'encre', 'm')
for i, (q, c) in enumerate([(1, 1), (2, 1), (3, 2), (4, 2), (6, 2), (12, 4)]):
    y = 62 - 9*i
    text(ax, 4, y, rf'$\varphi({q})$', 'sujet', 'm', ha='left')
    for j in range(c): box(ax, 30 + 7*j, y-3, 6, 6, 'sujet', r=0.3)
    text(ax, 30 + 7*c + 1, y, str(c), 'encre', 'm', ha='left')
save(fig, '46-253')
