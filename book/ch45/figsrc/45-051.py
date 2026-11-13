import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(64)
for x, g, r in ((14, 'G', 'sujet'), (44, 'G′', 'autre'), (74, 'G″', 'fixe')):
    text(ax, x, 57, g, r, 'l', weight='bold')
rows = [(42, '3', '¾ tour', '3'), (26, '2', '½ tour', '4')]
for y, a, b, c in rows:
    box(ax, 8, y-4, 12, 8, 'sujet', label=a); box(ax, 35, y-4, 18, 8, 'autre', label=b); box(ax, 68, y-4, 12, 8, 'fixe', label=c)
    arrow(ax, (21, y), (34, y), 'varie'); arrow(ax, (54, y), (67, y), 'varie')
text(ax, 27.5, 47, r'$\eta$', 'varie', 'm'); text(ax, 60.5, 47, r'$\zeta$', 'varie', 'm')
arrow(ax, (14, 20), (74, 20), 'resultat', curve=0.25, lw=1.3)
text(ax, 44, 7, r'$\eta$ puis $\zeta$ : un isomorphisme', 'resultat', 's')
save(fig, '45-051')
