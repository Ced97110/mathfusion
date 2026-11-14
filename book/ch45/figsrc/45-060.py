import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(64)
text(ax, 22, 56, r'$o(1)=4$', 'sujet', 'l'); text(ax, 66, 56, r'$o(2)=2$', 'varie', 'l')
text(ax, 22, 6, '4 pas pour revenir à 0', 'fixe', 's'); text(ax, 66, 6, '2 pas pour revenir à 0', 'fixe', 's')
for cx, role in ((22, 'sujet'), (66, 'varie')):
    P = ring(cx, 30, 11, 4)
    for i, p in enumerate(P):
        r = 'resultat' if i == 0 else ('sujet' if cx == 22 or i == 2 else 'fixe')
        disc(ax, p[0], p[1], 3.2, r, label=str(i))
    if cx == 22:
        for i in range(4): link(ax, P[i], P[(i+1) % 4], 'varie', rd=3.6, curve=-0.15)
    else:
        link(ax, P[0], P[2], 'varie', rd=3.6, curve=-0.3); link(ax, P[2], P[0], 'varie', rd=3.6, curve=-0.3)
save(fig, '45-060')
