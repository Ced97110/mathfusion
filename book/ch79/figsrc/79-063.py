import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(80)
text(ax, 22, 72, r'$\mathbb{F}_2=\{0,1\}$', 'sujet', 'l')
for y, s in zip((60, 50, 40, 30), (r'$0+0=0$', r'$0+1=1$', r'$1+0=1$', r'$1+1=0$')):
    text(ax, 22, y, s, 'varie' if s.startswith('$1+1') else 'encre', 'm')
box(ax, 8, 26, 28, 8, 'varie', fill=False)
text(ax, 65, 66, r'$\mathbb{F}_2^2$', 'sujet', 'l')
pts = {(0, 0): (54, 30), (1, 0): (76, 30), (0, 1): (54, 50), (1, 1): (76, 50)}
for a, b in (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 0), (0, 1)), ((1, 0), (1, 1))): E(ax, pts[a], pts[b], 5)
for (i, j), p in pts.items(): N(ax, *p, '(%d, %d)' % (i, j), 'sujet', 5, 's')
text(ax, 65, 16, '4 couples', 'resultat', 'm')
save(fig, '79-063')
