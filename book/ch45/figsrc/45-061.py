import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def link(ax, p, q, role='varie', rd=3.0, curve=0.0, lw=1.0, both=False):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*rd, p[1]+uy*rd), (q[0]-ux*rd, q[1]-uy*rd), role, lw, curve, both)
def ring(cx, cy, R, n):
    return [(cx + R*math.cos(math.radians(90 - 360*i/n)), cy + R*math.sin(math.radians(90 - 360*i/n))) for i in range(n)]

fig, ax = canvas(68)
text(ax, 44, 56, r'$o(a)$', 'sujet', 26)
text(ax, 16, 36, 'o : première lettre\nde « ordre »', 'varie', 's'); arrow(ax, (24, 41), (37, 51), 'varie')
text(ax, 72, 36, 'a : un élément\ndu groupe', 'sujet', 's'); arrow(ax, (66, 41), (48, 51), 'sujet')
for cx, n in ((22, 4), (66, 2)):
    text(ax, cx, 20, r'$o(%d)=%d$' % (1 if n == 4 else 2, n), 'resultat', 'm')
    for k in range(n): disc(ax, cx + (k - (n - 1) / 2) * 7, 12, 2.4, 'varie')
text(ax, 44, 3, 'un point = un pas', 'fixe', 's')
save(fig, '45-061')
