import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(68)
text(ax, 44, 63, 'à isomorphisme près', 'encre', 'm', weight='bold')
for y, t in ((46, 'horloge'), (34, 'rotations du carré'), (22, 'restes modulo 5')):
    box(ax, 2, y, 40, 9, 'sujet', label=t, size='s')
box(ax, 2, 6, 40, 9, 'autre', label='symétries du rectangle', size='s')
box(ax, 58, 24, 28, 28, 'resultat', label='entrée 1', size='m')
box(ax, 58, 6, 28, 12, 'resultat', label='entrée 2', size='m')
for y, ty in ((50.5, 46), (38.5, 38), (26.5, 30)):
    arrow(ax, (43, y), (57, ty), 'sujet')
arrow(ax, (43, 10.5), (57, 12), 'autre')
save(fig, '45-055')
