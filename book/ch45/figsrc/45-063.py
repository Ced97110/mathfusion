import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(56)
text(ax, 40, 51, 'une case = un pas, vert = 0', 'fixe', 's')
rows = [(38, [1, 2, 3, 0], 'sujet'), (24, [2, 0], 'varie'), (10, [3, 2, 1, 0], 'autre')]
for y, seq, role in rows:
    for k, v in enumerate(seq):
        box(ax, 4 + 13 * k, y, 11, 8, 'resultat' if v == 0 else role, label=str(v), size='m')
    text(ax, 70, y + 4, 'ordre %d' % len(seq), role, 'm', ha='left', weight='bold')
save(fig, '45-063')
