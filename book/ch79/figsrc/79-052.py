import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(84)
text(ax, 22, 77, 'notation du livre', 'fixe', 's'); text(ax, 66, 77, 'notation de Judson', 'fixe', 's')
box(ax, 6, 62, 32, 10, 'sujet', label=r'$a\leq b$'); box(ax, 50, 62, 32, 10, 'autre', label=r'$a\preceq b$')
text(ax, 44, 67, '=', 'encre', 'l')
box(ax, 14, 40, 60, 10, 'resultat', label='« $a$ est en dessous de $b$ »')
arrow(ax, (22, 62), (34, 50.5), 'fixe'); arrow(ax, (66, 62), (54, 50.5), 'fixe')
text(ax, 44, 32, 'pour la divisibilité', 'fixe', 's')
box(ax, 4, 14, 38, 10, 'resultat', label=r'$6\preceq12$ : vrai'); box(ax, 46, 14, 38, 10, 'limite', label=r'$5\preceq12$ : faux')
save(fig, '79-052')
