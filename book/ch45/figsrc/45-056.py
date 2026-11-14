import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(70)
text(ax, 44, 65, 'ℤ : tous les entiers', 'sujet', 'm', weight='bold')
f = numberline(ax, 12, 68, 50, -1, 3, 1, role='fixe', arrow_right=True)
arrow(ax, (12, 50), (7, 50), 'fixe', lw=0.9)
for v in range(-1, 3):
    arrow(ax, (f(v)+0.8, 51.6), (f(v+1)-0.8, 51.6), 'varie', curve=-0.7)
text(ax, f(-0.5), 58.5, r'$+1$', 'varie', 's')
pts = ring(24, 20, 12, 4)
for i in range(4):
    link(ax, pts[i], pts[(i+1) % 4], 'varie', rd=3.7, curve=-0.3)
for i, p in enumerate(pts): disc(ax, p[0], p[1], 3.2, 'sujet', label=str(i), size='s')
text(ax, 64, 24, 'ℤ/rℤ : r éléments', 'sujet', 'm', weight='bold'); text(ax, 64, 16, 'ici r = 4', 'fixe', 's')
text(ax, 64, 8, 'un seul groupe par sorte', 'resultat', 's', weight='bold')
save(fig, '45-056')
