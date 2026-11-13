import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(70)
ys = [40, 30, 20, 10]; rot = ['0', '¼', '½', '¾']
text(ax, 44, 63, r'$\eta$ : G vers G′', 'varie', 'm')
text(ax, 44, 57, r'$\eta^{-1}$ : G′ vers G', 'resultat', 'm')
text(ax, 14, 49, 'G', 'sujet', 'l', weight='bold'); text(ax, 74, 49, 'G′ (tours)', 'autre', 'l', weight='bold')
for n, y in enumerate(ys):
    disc(ax, 14, y, 3.6, 'sujet', label=str(n)); disc(ax, 74, y, 3.6, 'autre', label=rot[n])
    arrow(ax, (19, y+1.3), (69, y+1.3), 'varie'); arrow(ax, (69, y-1.3), (19, y-1.3), 'resultat')
save(fig, '45-050')
