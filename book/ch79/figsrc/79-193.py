import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
PD = {1: (0, 0), 2: (1, 0), 3: (0, 1), 4: (2, 0), 6: (1, 1), 8: (3, 0), 12: (2, 1), 24: (3, 1)}
ED = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 8), (4, 12), (6, 12), (8, 24), (12, 24)]
def pos(n, cx=50, y0=20, dx=12, dy=11):
    a, b = PD[n]
    return (cx + (b - a) * dx, y0 + (a + b) * dy)
def hasse(ax, roles, nodes=None, ered=None, hollow=(), r=3.6, **kw):
    nodes = nodes or list(PD); ered = ered or {}
    for p, q in ED:
        if p in nodes and q in nodes:
            (x1, y1), (x2, y2) = pos(p, **kw), pos(q, **kw)
            d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
            line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], ered.get((p, q), 'fixe'), lw=1.6 if (p, q) in ered else 0.9)
    for n in nodes:
        x, y = pos(n, **kw)
        disc(ax, x, y, r, roles.get(n, 'fixe'), fill=n not in hollow, label=str(n), size='s')
Y0 = 22
fig, ax = canvas(72)
hasse(ax, {4: 'sujet', 3: 'sujet', 12: 'resultat', 1: 'resultat'}, y0=Y0)
for k in range(5):
    text(ax, 84, Y0 + 11 * k, r'$d=%d$' % k, 'fixe', 's', ha='right')
text(ax, 44, 9, r'$d(12)+d(1)=3+0$' + '\n' + r'$d(4)+d(3)=2+1$', 'encre', 'm')
save(fig, '79-193')
