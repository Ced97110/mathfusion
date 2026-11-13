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
fig, ax = canvas(92)
text(ax, 22, 86, 'calcul direct', 'fixe', 's'); text(ax, 66, 86, 'par le produit', 'fixe', 's')
ring(ax, 13, 70, 5, [None]*2, 'sujet', r=2.2); ring(ax, 33, 70, 5, [None]*2, 'sujet', r=2.2)
text(ax, 13, 58, r'$(1\ 5)$ : 1', 'sujet', 's'); text(ax, 33, 58, r'$(3\ 8)$ : 1', 'sujet', 's')
text(ax, 22, 47, r'$1+1=2$ : pair', 'resultat', 'm')
text(ax, 66, 72, r'$\mathrm{sg}(\sigma)=+1$', 'sujet', 'm')
text(ax, 66, 62, r'$(+1)\times(+1)$', 'encre', 'm')
text(ax, 66, 52, r'$\mathrm{sg}(\sigma^2)=+1$', 'resultat', 'm')
arrow(ax, (22, 42), (32, 33), 'fixe'); arrow(ax, (66, 47), (56, 33), 'fixe')
box(ax, 10, 14, 68, 18, 'resultat', label='les deux donnent : paire', size='m')
save(fig, '46-247')
