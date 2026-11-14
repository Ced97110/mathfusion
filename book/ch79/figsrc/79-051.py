import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(74)
text(ax, 22, 66, 'en dessous de', 'fixe', 's'); text(ax, 66, 66, 'différent de', 'fixe', 's')
box(ax, 6, 52, 32, 9, 'sujet', label=r'$4\leq12$'); box(ax, 50, 52, 32, 9, 'autre', label=r'$4\neq12$')
text(ax, 44, 56.5, 'et', 'encre', 's')
box(ax, 28, 32, 32, 9, 'resultat', label=r'$4<12$')
arrow(ax, (22, 52), (38, 41.5), 'varie'); arrow(ax, (66, 52), (50, 41.5), 'varie')
xs = (24, 44, 64)
E(ax, (xs[0], 14), (xs[1], 14)); E(ax, (xs[1], 14), (xs[2], 14))
for x, s in zip(xs, ('4', '12', '60')): N(ax, x, 14, s)
text(ax, 44, 24, r'$4<12<60$', 'sujet', 'm')
save(fig, '79-051')
