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
fig, ax = canvas(56)
disc(ax, 12, 34, 4, 'sujet', label='2'); disc(ax, 44, 34, 4, 'fixe', label='5'); disc(ax, 76, 34, 4, 'resultat', label='2')
a, b = sh((12, 34), (44, 34), 4.6); arrow(ax, a, b, 'autre')
a, b = sh((44, 34), (76, 34), 4.6); arrow(ax, a, b, 'sujet')
text(ax, 28, 39, r'$\beta$', 'autre', 'm'); text(ax, 60, 39, r'$\alpha$', 'sujet', 'm')
text(ax, 28, 26, 'cycle de droite', 'autre', 's'); text(ax, 60, 26, 'cycle de gauche', 'sujet', 's')
text(ax, 44, 12, 'le produit laisse 2 en place', 'resultat', 'm', weight='bold')
save(fig, '46-249')
