import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(56)
heads = [r'$1_S$', r'$\alpha$', r'$\beta$', r'$\gamma$']
cw = 19.0; x0 = 6
text(ax, 44, 52, r'ligne de $\beta$ dans $M(\{1,2\})$', 'limite', 's', weight='bold')
for i, hd in enumerate(heads):
    text(ax, x0 + (i + .5) * cw, 43, hd, 'encre', 'm')
    box(ax, x0 + i * cw + .5, 27, cw - 1, 12, 'limite', label=r'$\beta$', size='l')
brace(ax, x0 + .5, x0 + 4 * cw - .5, 26, 'limite', label='quatre fois la même case', size='s')
text(ax, 22, 6, r'$\beta\circ\alpha=\beta\circ 1_S$', 'encre', 'm')
text(ax, 64, 6, r'et pourtant $\alpha\neq 1_S$', 'limite', 'm')
save(fig, '44-212')
