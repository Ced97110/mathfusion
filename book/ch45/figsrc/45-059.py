import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(76)
text(ax, 44, 66, r'$|G|$', 'sujet', 24)
text(ax, 20, 49, 'les barres :\nnombre d’éléments de', 'varie', 's'); arrow(ax, (27, 54), (38, 61), 'varie')
text(ax, 70, 49, 'G : un groupe', 'sujet', 's'); arrow(ax, (66, 54), (50, 61), 'sujet')
for cx, g, r in ((22, 'G', 'sujet'), (66, 'G′', 'autre')):
    text(ax, cx, 38, g, r, 'l', weight='bold')
    for k in range(4): disc(ax, cx - 4 + 8 * (k % 2), 30 - 8 * (k // 2), 2.8, r)
text(ax, 44, 26, '=', 'resultat', 'xl')
text(ax, 44, 8, r"$|G|=|G'|$", 'resultat', 'l')
save(fig, '45-059')
