import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(56)
f = numberline(ax, 10, 66, 24, 0, 6, 1, role='fixe', arrow_right=True)
for v in range(6):
    link(ax, (f(v), 25.5), (f(v+1), 25.5), 'varie', rd=0.9, curve=-0.8)
disc(ax, f(0), 24, 2.4, 'resultat')
text(ax, 15, 44, '0 = neutre', 'resultat', 's'); arrow(ax, (11, 40.5), (f(0), 28), 'resultat')
text(ax, 14, 36, r'$+1$', 'varie', 's')
text(ax, 80, 24, '…', 'fixe', 'l')
text(ax, 58, 44, 'jamais de retour à 0', 'limite', 's')
text(ax, 44, 7, 'ordre de 1 : infini', 'sujet', 'l', weight='bold')
save(fig, '45-062')
