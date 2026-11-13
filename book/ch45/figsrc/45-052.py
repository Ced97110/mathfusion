import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(74)
text(ax, 2, 60, 'lui-même', 'encre', 's', ha='left'); text(ax, 2, 38, 'dans les deux sens', 'encre', 's', ha='left'); text(ax, 2, 14, 'en chaîne', 'encre', 's', ha='left')
disc(ax, 62, 58, 4, 'sujet', label='G')
arrow(ax, (64.5, 61.6), (59.5, 61.6), 'resultat', curve=1.5)
disc(ax, 52, 36, 4, 'sujet', label='G'); disc(ax, 74, 36, 4, 'autre', label='G′')
arrow(ax, (56.5, 36), (69.5, 36), 'resultat', both=True)
for x, g, r in ((46, 'G', 'sujet'), (62, 'G′', 'autre'), (78, 'G″', 'fixe')):
    disc(ax, x, 14, 4, r, label=g)
arrow(ax, (50.5, 14), (57.5, 14), 'varie'); arrow(ax, (66.5, 14), (73.5, 14), 'varie')
arrow(ax, (46, 18.2), (78, 18.2), 'resultat', curve=-0.35)
save(fig, '45-052')
