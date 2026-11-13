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
fig, ax = canvas(90)
ring(ax, 22, 74, 8, [None]*4, 'sujet', r=2.2)
ring(ax, 62, 74, 5, [None]*2, 'autre', r=2.2)
text(ax, 22, 58, r'$(1\ 3\ 5\ 8)$', 'sujet', 's'); text(ax, 22, 52.5, r'$4-1=3$', 'sujet', 's')
text(ax, 62, 58, r'$(2\ 6)$', 'autre', 's'); text(ax, 62, 52.5, r'$2-1=1$', 'autre', 's')
text(ax, 44, 43, r'$N(\sigma)=3+1=4$ : pair', 'resultat', 'm')
text(ax, 44, 35, r'$\mathrm{sg}(\sigma)=+1$', 'resultat', 'l', weight='bold')
text(ax, 44, 27, 'confirmé par 4 échanges', 'fixe', 's')
for i, s in enumerate((r'$(1\ 8)$', r'$(1\ 5)$', r'$(1\ 3)$', r'$(2\ 6)$')):
    box(ax, 2 + 21.5*i, 10, 19, 10, 'varie', label=s, size='s')
save(fig, '46-246')
