import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(80)
box(ax, 2, 58, 52, 16, 'sujet', fill=False, dash=True)
for x in (12, 28, 44): E(ax, (28, 40), (x, 66))
E(ax, (28, 14), (28, 40))
for x, s in zip((12, 28, 44), ('12', '20', '30')): N(ax, x, 66, s)
N(ax, 28, 40, '2', 'resultat'); N(ax, 28, 14, '1', 'fixe')
text(ax, 70, 66, r'$A=\{12,20,30\}$', 'sujet', 'm')
text(ax, 68, 40, r'$\inf A=2$', 'resultat', 'l'); text(ax, 68, 34, 'plus grand minorant', 'resultat', 's')
text(ax, 68, 14, 'autre minorant', 'fixe', 's')
save(fig, '79-055')
