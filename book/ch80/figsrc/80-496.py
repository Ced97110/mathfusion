import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def seg(ax, a, b, r, role='fixe'):
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    line(ax, [(a[0]+u[0]*r, a[1]+u[1]*r), (b[0]-u[0]*r, b[1]-u[1]*r)], role)
cs = [(14, 10 + 14 * i) for i in range(4)]
for a, b in zip(cs, cs[1:]): seg(ax, a, b, 3.8)
for i, (x, y) in enumerate(cs): disc(ax, x, y, 3.8, 'sujet', label=str(i), size='s')
text(ax, 18, 64, 'une chaîne :\ntous se comparent', 'sujet', 's')
P = {1: (64, 10), 2: (54, 24), 3: (74, 24), 4: (44, 38), 6: (64, 38), 12: (54, 52)}
for a, b in [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)]: seg(ax, P[a], P[b], 3.8)
line(ax, [(48, 38), (60, 38)], 'limite', dash=True)
for k, (x, y) in P.items(): disc(ax, x, y, 3.8, 'limite' if k in (4, 6) else 'autre', label=str(k), size='s')
text(ax, 62, 64, 'diviseurs de 12 : 4 et 6\nne se comparent pas', 'limite', 's')
save(fig, '80-496')
