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
fig, ax = canvas(80)
text(ax, 22, 74, 'les nombres', 'fixe', 's'); text(ax, 66, 74, 'les permutations', 'fixe', 's')
for i in range(3):
    for j in range(5): disc(ax, 5 + 4*j + 1, 58 - 4*i, 1.3, 'sujet')
for i in range(5):
    for j in range(3): disc(ax, 31 + 4*j, 62 - 4*i, 1.3, 'sujet')
text(ax, 25, 54, '=', 'resultat', 'l')
text(ax, 13, 42, r'$3\times 5$', 'sujet', 's'); text(ax, 35, 42, r'$5\times 3$', 'sujet', 's')
text(ax, 22, 32, 'ordre sans effet', 'resultat', 's')
line(ax, [(44, 30), (44, 72)], 'fixe', lw=0.5, dash=True)
text(ax, 66, 62, r'$\alpha\beta$ : 1 $\to$ 3', 'sujet', 'm'); text(ax, 66, 52, r'$\beta\alpha$ : 1 $\to$ 4', 'autre', 'm')
text(ax, 66, 42, r'$3\neq 4$', 'limite', 'l', weight='bold'); text(ax, 66, 32, 'l’ordre compte', 'limite', 's')
save(fig, '46-251')
