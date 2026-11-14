import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(70)
text(ax, 28, 64, 'une classe', 'sujet', 'm', weight='bold'); text(ax, 74, 64, 'une autre classe', 'autre', 'm', weight='bold')
box(ax, 2, 6, 52, 52, 'sujet', fill=False, dash=True, lw=1.0)
for y, t in ((42, 'horloge ℤ/4ℤ'), (28, 'rotations du carré'), (14, 'restes modulo 5')):
    box(ax, 6, y, 44, 10, 'sujet', label=t, size='s')
box(ax, 62, 22, 24, 24, 'autre', fill=False, dash=True, lw=1.0)
box(ax, 64.5, 28, 19, 12, 'autre', label='symétries\ndu rectangle', size='s')
text(ax, 58, 34, '≠', 'limite', 'xl')
save(fig, '45-053')
