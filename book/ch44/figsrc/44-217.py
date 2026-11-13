import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(72)
xs = [12, 44, 76]; ys = [48, 34, 20]
text(ax, xs[0], 63, 'départ', 'encre', 's'); text(ax, xs[1], 63, r'après $\sigma$', 'varie', 's'); text(ax, xs[2], 63, r'après $\tau_1$', 'sujet', 's')
for j in range(3):
    k = j + 1; m = P['s'][j]; e = P['a'][m - 1]
    disc(ax, xs[0], ys[j], 3.4, 'fixe', label=str(k))
    disc(ax, xs[1], ys[j], 3.4, 'varie', label=str(m))
    disc(ax, xs[2], ys[j], 3.4, 'resultat' if e == k else 'sujet', label=str(e))
    arrow(ax, (xs[0] + 4, ys[j]), (xs[1] - 4, ys[j]), 'varie'); arrow(ax, (xs[1] + 4, ys[j]), (xs[2] - 4, ys[j]), 'sujet')
text(ax, 44, 9, r'$\tau_1\circ\sigma=\tau_2$', 'resultat', 'l', weight='bold')
save(fig, '44-217')
