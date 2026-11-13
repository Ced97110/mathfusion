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
ring(ax, 20, 78, 8, [None]*4, 'sujet', r=2.2)
ring(ax, 64, 78, 9, [None]*6, 'autre', r=2.2)
text(ax, 20, 64, 'cycle de longueur 4', 'sujet', 's')
text(ax, 64, 64, 'longueur 6', 'autre', 's')
text(ax, 2, 55, 'multiples de 4', 'sujet', 's', ha='left')
text(ax, 2, 41, 'multiples de 6', 'autre', 's', ha='left')
for i in range(12):
    v = i + 1; x = 8 + 6*i
    box(ax, x, 45, 6, 6, 'sujet' if v % 4 == 0 else 'fixe', fill=v % 4 == 0, r=0.3, lw=0.6)
    box(ax, x, 32, 6, 6, 'autre' if v % 6 == 0 else 'fixe', fill=v % 6 == 0, r=0.3, lw=0.6)
box(ax, 8 + 66 - 0.5, 30.5, 7, 22, 'resultat', fill=False, lw=1.2)
for v in (4, 6, 8, 12): text(ax, 8 + 6*(v-1) + 3, 26, str(v), 'resultat' if v == 12 else 'fixe', 's')
text(ax, 44, 14, r'$\mathrm{PPCM}(4,6)=12$', 'resultat', 'm', weight='bold')
save(fig, '46-243')
