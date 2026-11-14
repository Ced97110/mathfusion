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
fig, ax = canvas(70)
ring(ax, 18, 48, 9, ['1', '3', '5', '8'], 'sujet')
text(ax, 18, 32, '4-cycle', 'sujet', 's')
ring(ax, 18, 15, 5, [None]*2, 'autre', r=2.2)
text(ax, 31, 15, r'$(2\ 6)$', 'autre', 's', ha='left')
arrow(ax, (37, 44), (53, 44), 'varie')
text(ax, 45, 49, r'$\times 2$', 'varie', 's')
for x, l in ((62, ('1', '5')), (78, ('3', '8'))):
    disc(ax, x, 54, 2.6, 'resultat', label=l[0], size='s'); disc(ax, x, 40, 2.6, 'resultat', label=l[1], size='s')
    arrow(ax, (x, 50.8), (x, 43.2), 'resultat', both=True)
text(ax, 70, 31, 'deux 2-cycles', 'resultat', 's')
disc(ax, 62, 15, 2.2, 'fixe'); disc(ax, 78, 15, 2.2, 'fixe')
text(ax, 70, 6, r'$(2\ 6)$ : identité', 'fixe', 's')
save(fig, '46-245')
