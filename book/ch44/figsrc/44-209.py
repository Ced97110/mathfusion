import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(66)
n, cw = 6, 8.5
x0, ytop = 24, 58
for i, k in enumerate(ORDER):
    text(ax, x0 + (i + .5) * cw, ytop + 5, NM[k], 'sujet' if k == '1' else 'encre', 's', weight='bold' if k == '1' else 'normal')
    box(ax, x0 + i * cw + .3, ytop - cw + .3, cw - .6, cw - .6, 'resultat', label=NM[k], size='s', r=0.4, lw=0.6)
text(ax, x0 - 4.5, ytop - .5 * cw, '1', 'sujet', 's', weight='bold')
for r in range(1, n):
    for c in range(n):
        role = 'resultat' if c == 0 else 'fixe'
        box(ax, x0 + c * cw + .3, ytop - (r + 1) * cw + .3, cw - .6, cw - .6, role, r=0.4, lw=0.6)
text(ax, 44, 4, 'ligne et colonne de 1 : mêmes en-têtes', 'resultat', 's')
save(fig, '44-209')
