import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(80)
P = {'0': (44, 14), '1': (44, 66), 'a': (24, 40), 'b': (64, 30), 'c': (64, 50)}
for a, b in (('0', 'a'), ('a', '1'), ('0', 'b'), ('b', 'c'), ('c', '1')): E(ax, P[a], P[b])
line(ax, [(27.2, 41.2), (60.8, 48.8)], 'limite', dash=True)
for k in '01': N(ax, *P[k], '$%s$' % k, 'fixe')
N(ax, *P['a'], '$a$', 'autre')
for k in 'bc': N(ax, *P[k], '$%s$' % k, 'sujet')
text(ax, 70, 70, r'$N_5$ : pentagone', 'sujet', 'm')
text(ax, 22, 8, r'$a$ et $c$ : incomparables', 'limite', 's')
save(fig, '79-064')
