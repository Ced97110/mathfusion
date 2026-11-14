import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(85)
text(ax, 24, 78, r'$L(V)$', 'sujet', 'l')
for x in (8, 24, 40): E(ax, (24, 22), (x, 42), 4); E(ax, (x, 42), (24, 62), 4)
N(ax, 24, 62, r'$V$', 'sujet', 4); N(ax, 24, 22, r'$\{0\}$', 'fixe', 4, 's')
for x, k in zip((8, 24, 40), '123'): N(ax, x, 42, r'$d_%s$' % k, 'autre', 4, 's')
text(ax, 50, 42, r'$\ldots$', 'autre', 'm')
box(ax, 54, 22, 30, 40, 'sujet')
text(ax, 69, 67, r'plan $V$', 'sujet', 's')
cx, cy = 69, 42
for a in (0, 60, 120):
    t = math.radians(a); line(ax, [(cx - 13*math.cos(t), cy - 13*math.sin(t)), (cx + 13*math.cos(t), cy + 13*math.sin(t))], 'autre', lw=1.1)
disc(ax, cx, cy, 1.6, 'fixe')
text(ax, 69, 14, 'origine', 'fixe', 's')
arrow(ax, (69, 17.5), (69, 40), 'fixe')
save(fig, '79-062')
