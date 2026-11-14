import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(70)
for x in (10, 24, 38): E(ax, (x, 16), (24, 52))
for x, s in zip((10, 24, 38), ('12', '20', '30')): N(ax, x, 16, s)
N(ax, 24, 52, '60', 'resultat')
text(ax, 66, 52, r'$1=60$', 'resultat', 'l')
text(ax, 66, 38, r'$a\leq1$ pour tout $a$', 'sujet', 'm')
text(ax, 66, 24, r'$12\vee60=60$', 'resultat', 'm')
save(fig, '79-059')
