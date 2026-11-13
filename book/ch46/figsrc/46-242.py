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
fig, ax = canvas(98)
text(ax, 44, 91, r'$\sigma^m=\gamma_1^m\,\gamma_2^m$', 'encre', 'xl')
for i in range(8): text(ax, 14.5 + 9*i, 81, str(i+1), 'encre', 's')
rows = [(r'$\gamma_1^m$ : 4 divise $m$', 4, 'sujet', 74, 65), (r'$\gamma_2^m$ : 2 divise $m$', 2, 'autre', 60, 51),
        (r'$\sigma^m$ : les deux à la fois', 4, 'fixe', 46, 37)]
for lab, d, role, yl, yc in rows:
    text(ax, 10, yl, lab, role if role != 'fixe' else 'encre', 's', ha='left')
    for i in range(8):
        box(ax, 10 + 9*i, yc, 9, 7, 'resultat' if (i+1) % d == 0 else role, r=0.4, lw=0.6)
text(ax, 14.5 + 27, 31.5, 'plus petit : 4', 'resultat', 's')
text(ax, 44, 23, 'vert : le cycle est revenu', 'resultat', 's')
save(fig, '46-242')
