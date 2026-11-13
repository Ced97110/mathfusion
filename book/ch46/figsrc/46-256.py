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
fig, ax = canvas(84)
text(ax, 23, 77, 'ℤ/4ℤ', 'sujet', 'm'); text(ax, 66, 77, 'ℤ/2ℤ × ℤ/2ℤ', 'autre', 'm')
pts = ring(ax, 23, 45, 13, ['0', '1', '2', '3'], 'sujet', r=3.2, curve=-0.25)
a, b = sh(pts[0], pts[2], 3.8); line(ax, [a, b], 'varie', lw=1.4)
text(ax, 28, 45, r'$\{0,2\}$', 'varie', 's')
top = (66, 62); lows = [(48, 36), (66, 36), (84, 36)]
for l in lows:
    a, b = sh(top, l, 3.8); line(ax, [a, b], 'varie', lw=1.4)
disc(ax, top[0], top[1], 3.2, 'autre', label='00', size='s')
for l, s in zip(lows, ('01', '10', '11')): disc(ax, l[0], l[1], 3.2, 'autre', label=s, size='s')
text(ax, 23, 14, '1 sous-groupe propre', 'sujet', 's'); text(ax, 66, 14, '3 sous-groupes propres', 'autre', 's')
save(fig, '46-256')
