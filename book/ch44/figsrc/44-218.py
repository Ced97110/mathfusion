import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(66)
xm, xl, xr = 44, 12, 76; ys = [46, 32, 18]
text(ax, 21, 60, r'$\sigma\circ\tau_1=\tau_3$', 'varie', 's', weight='bold')
text(ax, 67, 60, r'$\tau_1\circ\sigma=\tau_2$', 'autre', 's', weight='bold')
text(ax, 44, 60, r'$\neq$', 'limite', 'l', weight='bold')
for j in range(3):
    k = j + 1
    el = P['s'][P['a'][j] - 1]; er = P['a'][P['s'][j] - 1]
    disc(ax, xm, ys[j], 3.4, 'fixe', label=str(k))
# end columns: row = final place of the vertex, label = vertex
for j in range(3):
    k = j + 1
    el = P['s'][P['a'][j] - 1]; er = P['a'][P['s'][j] - 1]
    arrow(ax, (xm - 4, ys[j]), (xl + 4, ys[el - 1]), 'varie', lw=1.0)
    arrow(ax, (xm + 4, ys[j]), (xr - 4, ys[er - 1]), 'autre', lw=1.0)
for p in range(3):
    disc(ax, xl, ys[p], 3.4, 'resultat' if P['s'][P['a'][p] - 1] == p + 1 else 'varie', label=str(p + 1))
    disc(ax, xr, ys[p], 3.4, 'resultat' if P['a'][P['s'][p] - 1] == p + 1 else 'autre', label=str(p + 1))
save(fig, '44-218')
