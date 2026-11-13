import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(66)
xs = (22, 66); ys = [48, 37, 26, 15]
text(ax, 22, 59, 'G', 'sujet', 'l', weight='bold'); text(ax, 66, 59, 'G', 'sujet', 'l', weight='bold')
text(ax, 44, 59, r'$\eta(x)=x$', 'varie', 'l')
for n, y in enumerate(ys):
    disc(ax, 22, y, 3.6, 'sujet', label=str(n)); disc(ax, 66, y, 3.6, 'sujet', label=str(n))
    arrow(ax, (26.5, y), (61.5, y), 'resultat')
text(ax, 44, 5, 'chaque nombre garde son nom', 'fixe', 's')
save(fig, '45-049')
