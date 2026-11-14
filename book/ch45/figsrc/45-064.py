import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(66)
text(ax, 44, 59, r"$|G|=|G'|$", 'resultat', 'l')
text(ax, 14, 59, 'G', 'sujet', 'l', weight='bold'); text(ax, 74, 59, 'G′', 'autre', 'l', weight='bold')
rot = ['0', '¼', '½', '¾']
for n in range(4):
    y = 46 - 10 * n
    disc(ax, 14, y, 3.4, 'sujet', label=str(n)); disc(ax, 74, y, 3.4, 'autre', label=rot[n])
    arrow(ax, (18.5, y), (69.5, y), 'varie')
text(ax, 14, 8, '4 éléments', 'sujet', 's'); text(ax, 74, 8, '4 éléments', 'autre', 's')
save(fig, '45-064')
