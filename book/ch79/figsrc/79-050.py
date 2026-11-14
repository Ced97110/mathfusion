import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(66)
text(ax, 44, 60, 'diviseurs de 60', 'fixe', 's')
for cx, ok in ((22, True), (66, False)):
    E(ax, (cx, 16), (cx, 46))
    N(ax, cx, 16, '4'); N(ax, cx, 46, '12')
    if ok: arrow(ax, (cx+9, 22), (cx+9, 40), 'resultat')
    else: arrow(ax, (cx+9, 40), (cx+9, 22), 'limite')
text(ax, 22, 6, r'$4\leq12$ : vrai', 'resultat', 'm')
text(ax, 66, 6, r'$12\leq4$ : faux', 'limite', 'm')
save(fig, '79-050')
