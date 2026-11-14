import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
o = (44, 10); u = 14.0
def P(x, y, z): return iso(x, y, z, o, u)
V = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
for p in V:
    for q in V:
        if sum(p[i] != q[i] for i in range(3)) == 1 and p < q:
            line(ax, [P(*p), P(*q)], 'fixe', lw=0.8)
line(ax, [P(0,0,0), P(1,1,1)], 'sujet', lw=1.8); line(ax, [P(1,0,0), P(0,1,1)], 'autre', lw=1.8)
disc(ax, *P(.5,.5,.5), 1.3, 'resultat')
for n, p, dx, dy in (('A', (0,0,0), -3, -2), ('B', (1,0,0), 3, -2), ('G', (1,1,1), 3, 2), ('H', (0,1,1), -3, 2)):
    text(ax, P(*p)[0]+dx, P(*p)[1]+dy, n, 'encre', 's')
c = P(.5,.5,.5)
text(ax, c[0]+20, c[1]+10, 'centre', 'resultat', 's')
arrow(ax, (c[0]+15, c[1]+8), (c[0]+1.8, c[1]-1), 'resultat', lw=0.8)
text(ax, 20, 52, 'AG', 'sujet', 'm'); text(ax, 68, 52, 'BH', 'autre', 'm')
save(fig, '27-132')
