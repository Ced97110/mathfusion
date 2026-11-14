import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
O, u = (27, 6), 11.0
P = lambda x, y, z: iso(x, y, z, O, u)
a, b, c = 1, 2, 2
# arêtes de la boîte 1 x 2 x 2 (cachées en pointillés)
V = {(i, j, k): P(i * a, j * b, k * c) for i in (0, 1) for j in (0, 1) for k in (0, 1)}
hidden = {frozenset([(1, 1, 0), (0, 1, 0)]), frozenset([(1, 1, 0), (1, 0, 0)]), frozenset([(1, 1, 0), (1, 1, 1)])}
for p in V:
    for q in V:
        if p < q and sum(abs(p[i] - q[i]) for i in range(3)) == 1:
            line(ax, [V[p], V[q]], 'fixe', lw=0.8, dash=frozenset([p, q]) in hidden)
A, D, B = P(0, 0, 0), P(a, b, 0), P(a, b, c)
assert abs(math.hypot(a, b) ** 2 - 5) < 1e-9 and abs(math.sqrt(5 + c * c) - 3) < 1e-9
line(ax, [A, D], 'varie', lw=1.6, dash=True)
line(ax, [D, B], 'sujet', lw=1.6, dash=True)
arrow(ax, A, B, 'resultat', lw=1.8)
text(ax, 31, 4.5, '1', 'fixe', 's')
text(ax, 11.5, 14, '2', 'fixe', 's')
text(ax, 41, 22, '2', 'fixe', 's')
text(ax, 18, 25, r'$\sqrt{5}$', 'varie', 's')
text(ax, 38.5, 40, '3', 'resultat', 'm', weight='bold')
text(ax, 62, 52, 'Pythagore, 2 fois', 'encre', 'm')
text(ax, 50, 40, r'$1^2+2^2=5$', 'varie', 's', ha='left')
text(ax, 50, 28, r'$5+2^2=9$', 'sujet', 's', ha='left')
text(ax, 50, 16, r'$\sqrt{9}=3$', 'resultat', 'm', ha='left')
save(fig, '41-050')
