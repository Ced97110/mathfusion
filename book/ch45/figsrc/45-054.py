import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(60)
text(ax, 24, 55, '3 lignes dans la liste', 'limite', 's'); text(ax, 72, 55, 'même table', 'resultat', 's')
for y, t in ((38, 'horloge à quatre heures'), (24, r'$1,\ i,\ -1,\ -i$ avec $\times$'), (10, 'rotations du carré')):
    box(ax, 2, y, 48, 11, 'sujet', label=t, size='s'); arrow(ax, (51, y+5.5), (60, 29), 'varie')
box(ax, 61, 18, 25, 22, 'resultat', label='un seul\ngroupe', size='m')
save(fig, '45-054')
