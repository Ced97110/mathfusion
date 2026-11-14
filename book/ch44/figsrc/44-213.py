import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(62)
cw = 13.0; x0 = 5
for i, k in enumerate(ORDER):
    hl = (k == 'q')
    text(ax, x0 + (i + .5) * cw, 50, NM[k], 'sujet' if hl else 'encre', 'm', weight='bold' if hl else 'normal')
    res = comp('s', k)
    box(ax, x0 + i * cw + .5, 28, cw - 1, 14, 'resultat' if res == '1' else 'fixe', label=NM[res], size='l', weight='bold' if res == '1' else 'normal')
xq = x0 + 2.5 * cw
arrow(ax, (xq, 27.5), (xq, 17), 'varie', lw=1.2)
text(ax, xq, 12, r'$\sigma^{-1}=\sigma^2$', 'varie', 'l')
text(ax, 44, 59, r'ligne de $\sigma$ : où est le 1 ?', 'sujet', 's')
save(fig, '44-213')
