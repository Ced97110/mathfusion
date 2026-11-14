import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(80)
box(ax, 3, 6, 54, 68, 'fixe', fill=False, dash=True)
E(ax, (30, 14), (14, 40)); E(ax, (30, 14), (46, 40)); E(ax, (14, 40), (30, 66)); E(ax, (46, 40), (30, 66))
N(ax, 30, 14, '4'); N(ax, 14, 40, '12', 'resultat'); N(ax, 46, 40, '20', 'resultat'); N(ax, 30, 66, '60')
text(ax, 20, 14, r'$a$', 'sujet', 'm'); text(ax, 20, 66, r'$b$', 'sujet', 'm')
text(ax, 72, 66, r'$I[4,60]$', 'sujet', 'l')
text(ax, 72, 52, r'$\{4,12,20,60\}$', 'resultat', 'm')
text(ax, 72, 38, r'$4\leq x\leq60$', 'sujet', 'm')
save(fig, '79-061')
