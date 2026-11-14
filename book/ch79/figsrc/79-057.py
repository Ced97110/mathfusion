import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(76)
E(ax, (44, 20), (56, 46)); E(ax, (68, 20), (56, 46))
N(ax, 44, 20, '4'); N(ax, 68, 20, '6', 'autre'); N(ax, 56, 46, '12', 'varie')
arrow(ax, (52, 43), (40.5, 23.5), 'resultat', curve=-0.25)
text(ax, 62, 46, r'$4\vee6=12$', 'varie', 'm', ha='left')
text(ax, 22, 36, r'$12\wedge4=4$', 'resultat', 'm')
box(ax, 14, 4, 60, 10, 'resultat', label=r'$(4\vee6)\wedge4=4$')
save(fig, '79-057')
