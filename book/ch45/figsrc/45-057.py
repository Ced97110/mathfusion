import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(66)
text(ax, 22, 60, '4 éléments : 2 groupes', 'encre', 's', weight='bold'); text(ax, 67, 60, '5 éléments : 1 groupe', 'encre', 's', weight='bold')
line(ax, [(46, 4), (46, 62)], 'fixe', dash=True)
p4 = ring(16, 44, 8, 4)
for i in range(4): link(ax, p4[i], p4[(i+1) % 4], 'varie', rd=3.0, curve=-0.3, lw=0.8)
for p in p4: disc(ax, p[0], p[1], 2.6, 'sujet')
text(ax, 28, 44, 'horloge', 'sujet', 's', ha='left')
poly(ax, [(8, 11), (24, 11), (24, 21), (8, 21)], 'autre', fill=False)
for (x, y) in [(8, 11), (24, 11), (24, 21), (8, 21)]: disc(ax, x, y, 2.6, 'autre')
text(ax, 28, 16, 'rectangle', 'autre', 's', ha='left')
text(ax, 16, 30, '≠', 'limite', 'xl')
p5 = ring(67, 36, 11, 5)
for i in range(5): link(ax, p5[i], p5[(i+1) % 5], 'varie', rd=3.0, curve=-0.25, lw=0.8)
for p in p5: disc(ax, p[0], p[1], 2.6, 'resultat')
text(ax, 67, 16, r'$\mathbb{Z}/5\mathbb{Z}$', 'resultat', 'm'); text(ax, 67, 9, '5 est premier', 'fixe', 's')
save(fig, '45-057')
