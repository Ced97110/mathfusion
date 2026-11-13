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
fig, ax = canvas(82)
def rowf(y, lab, role, nodes, fin, labs, dash=False):
    text(ax, 2, y+12, lab, role, 's', ha='left')
    xs = (10, 44, 78)
    for k, (x, n) in enumerate(zip(xs, nodes)):
        disc(ax, x, y, 4, fin if k == 2 else 'fixe', label=n)
    for k in range(2):
        a, b = sh((xs[k], y), (xs[k+1], y), 4.6)
        arrow(ax, a, b, 'fixe'); text(ax, (xs[k]+xs[k+1])/2, y+5, labs[k], 'encre', 'm')
rowf(62, r'$\alpha\beta$ : $\beta$ d’abord, puis $\alpha$', 'sujet', ('1', '3', '3'), 'sujet', (r'$\beta$', r'$\alpha$'))
rowf(30, r'$\beta\alpha$ : $\alpha$ d’abord, puis $\beta$', 'autre', ('1', '6', '4'), 'autre', (r'$\alpha$', r'$\beta$'))
text(ax, 44, 8, r'$3\neq 4$', 'encre', 'l', weight='bold')
save(fig, '46-250')
