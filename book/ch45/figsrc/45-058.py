import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(62)
data = [(16, 'horloge', 4), (44, 'rotations\ndu carré', 4), (72, 'permutations\nde 3 objets', 6)]
for x, name, n in data:
    text(ax, x, 54, name, 'sujet', 's', weight='bold')
    for k in range(n):
        disc(ax, x - 3.8 + 7.6 * (k % 2), 40 - 8 * (k // 2), 2.8, 'sujet')
    text(ax, x, 12, r'$|G|=%d$' % n, 'resultat', 'l')
save(fig, '45-058')
