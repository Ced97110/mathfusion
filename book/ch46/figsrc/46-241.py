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
ring(ax, 20, 76, 9, ['1', '3', '5', '8'], 'sujet')
ring(ax, 66, 76, 6, ['2', '6'], 'autre')
text(ax, 20, 62, 'cycle de longueur 4', 'sujet', 's')
text(ax, 66, 62, 'longueur 2', 'autre', 's')
f = numberline(ax, 8, 80, 27, 0, 12, labels=False, arrow_right=False)
text(ax, 2, 54, 'multiples de 4', 'sujet', 's', ha='left')
text(ax, 2, 41, 'multiples de 2', 'autre', 's', ha='left')
for v in (4, 8, 12): disc(ax, f(v), 48, 2.2, 'sujet')
for v in range(2, 13, 2): disc(ax, f(v), 35, 2.2, 'autre')
box(ax, f(4)-3.5, 31, 7, 21, 'resultat', fill=False, lw=1.2)
for v in (4, 8, 12): text(ax, f(v), 22.6, str(v), 'resultat' if v == 4 else 'fixe', 's')
text(ax, 44, 14, r'$o(\sigma)=\mathrm{PPCM}(4,2)=4$', 'resultat', 'm', weight='bold')
save(fig, '46-241')
