import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(80)
box(ax, 10, 6, 44, 16, 'sujet', fill=False, dash=True)
E(ax, (20, 14), (32, 40)); E(ax, (44, 14), (32, 40)); E(ax, (32, 40), (32, 66))
N(ax, 20, 14, '4'); N(ax, 44, 14, '6'); N(ax, 32, 40, '12', 'resultat'); N(ax, 32, 66, '60', 'fixe')
text(ax, 70, 14, r'$A=\{4,6\}$', 'sujet', 'm')
text(ax, 70, 40, r'$\sup A=12$', 'resultat', 'l'); text(ax, 70, 34, 'plus petit majorant', 'resultat', 's')
text(ax, 70, 66, 'autre majorant', 'fixe', 's')
save(fig, '79-054')
