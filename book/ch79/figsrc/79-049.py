import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(72)
P = {'p': (28, 18), 'q': (60, 18), 'r': (28, 48), 's': (60, 48)}
for a in 'pq':
    for b in 'rs': E(ax, P[a], P[b])
for k in 'pq': N(ax, *P[k], '$%s$' % k, 'sujet')
for k in 'rs': N(ax, *P[k], '$%s$' % k, 'autre')
line(ax, [(31.4, 48), (56.6, 48)], 'limite', dash=True)
text(ax, 44, 44.3, 'incomparables', 'limite', 's')
brace(ax, 22, 66, 55, 'autre', label=r'majorants de $p$ et $q$', down=False)
text(ax, 44, 7, r'$p\vee q$ n’existe pas', 'limite', 'l')
save(fig, '79-049')
