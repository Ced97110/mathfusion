import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(56)
w, g, x0 = 12.6, 1.2, 4.6
text(ax, 44, 52, 'les 6 mouvements du triangle', 'sujet', 's', weight='bold')
text(ax, 44, 4, r'les $3!=6$ rangements de 1, 2, 3', 'autre', 's', weight='bold')
for i, k in enumerate(ORDER):
    x = x0 + i * (w + g)
    box(ax, x, 36, w, 10, 'sujet', label=NM[k], size='m')
    box(ax, x, 10, w, 10, 'autre', label=''.join(map(str, P[k])), size='m')
    arrow(ax, (x + w / 2, 35.6), (x + w / 2, 20.4), 'resultat', lw=1.1)
save(fig, '44-215')
