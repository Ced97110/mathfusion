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
text(ax, 44, 64, r'$\sigma^2=(1\ 5)(3\ 8)$', 'encre', 'l')
f = lambda i: 8 + (i-1)*72/7
for i in range(1, 9):
    disc(ax, f(i), 34, 3.0, 'sujet' if i in (1, 3, 5, 8) else 'fixe', label=str(i), size='s')
a, b = sh((f(1), 34), (f(5), 34), 3)
arrow(ax, (a[0], 37.4), (b[0], 37.4), 'varie', both=True, curve=-0.45)
a, b = sh((f(3), 34), (f(8), 34), 3)
arrow(ax, (a[0], 30.6), (b[0], 30.6), 'varie', both=True, curve=0.35)
text(ax, (f(1)+f(5))/2, 52, r'$(1\ 5)$', 'varie', 's')
text(ax, (f(3)+f(8))/2, 15, r'$(3\ 8)$', 'varie', 's')
text(ax, 44, 6, '2, 4, 6 et 7 : en place', 'fixe', 's')
save(fig, '46-244')
