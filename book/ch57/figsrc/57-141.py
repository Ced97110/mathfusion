import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 9.0; ox, oy = 22.0, 33.0
P = lambda x, y: (ox + x * u, oy + y * u)
A = {(-1, -1), (1, 0), (3, 1), (5, 2)}      # classe de (1;0) : x - 2y = 1
B = {(-1, -2), (1, -1), (3, 0), (5, 1)}     # classe de (3;0) : x - 2y = 3
line(ax, [P(-2, -1.5), P(6, 2.5)], 'autre', lw=1.2)
line(ax, [P(-1, -2), P(6, 1.5)], 'resultat', lw=1.2)
for i in range(-2, 7):
    for j in range(-2, 3):
        if (i, j) in A or (i, j) in B: continue
        disc(ax, *P(i, j), 0.5, 'fixe')
for p in A: disc(ax, *P(*p), 1.1, 'autre')
for p in B: disc(ax, *P(*p), 1.1, 'resultat')
a, b = P(1, 0), P(3, 0)
arrow(ax, (a[0] + 1.6, a[1] + 0.2), (b[0] - 1.6, b[1] + 0.2), 'varie', lw=1.6, curve=0)
text(ax, P(2, 0)[0], P(2, 0)[1] + 3.8, r'$\times 3$', 'varie', 's')
text(ax, a[0] - 8, a[1] + 3.5, r'$(1\,;\,0)$', 'autre', 's')
text(ax, b[0] + 3, b[1] - 4.2, r'$(3\,;\,0)$', 'resultat', 's')
text(ax, P(0, 1.5)[0] - 6, P(0, 1.5)[1] + 6, r'classe de $(1\,;\,0)$', 'autre', 's')
text(ax, 72, 36.3, r'classe de $(3\,;\,0)$', 'resultat', 's')
text(ax, 44, 60, r'$3\cdot\overline{(1\,;\,0)}=\overline{3\cdot(1\,;\,0)}$', 'encre', 'm')
save(fig, '57-141')
