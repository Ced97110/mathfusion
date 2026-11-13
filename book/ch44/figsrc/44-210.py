import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(52)
cw = 13.0; x0 = 5
for i, k in enumerate(ORDER):
    text(ax, x0 + (i + .5) * cw, 43, NM[k], 'encre', 'm')
    res = comp('s', k)
    box(ax, x0 + i * cw + .5, 22, cw - 1, 14, 'resultat', label=NM[res], size='l')
    arrow(ax, (x0 + (i + .5) * cw, 40.5), (x0 + (i + .5) * cw, 36.8), 'fixe', lw=0.8)
text(ax, 44, 49.5, r'ligne de $\sigma$', 'sujet', 's')
brace(ax, x0 + .5, x0 + 6 * cw - .5, 21, 'resultat', label='6 résultats tous différents', size='s')
save(fig, '44-210')
