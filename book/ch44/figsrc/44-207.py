import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(62)
ROLE = {'1': 'fixe', 's': 'varie', 'q': 'varie', 'a': 'sujet', 'b': 'sujet', 'c': 'sujet'}
w, h, gap = 26, 22, 2.5
for i, k in enumerate(ORDER):
    r, c = divmod(i, 3)
    x = 2 + c * (w + gap); y = 35 - r * (h + 3)
    box(ax, x, y, w, h, ROLE[k], size='l')
    text(ax, x + w / 2, y + h - 5, NM[k], ROLE[k], 'l', weight='bold')
    p = P[k]
    text(ax, x + w / 2, y + 8, r'$' + r',\ '.join(f'{j+1}\\!\\to\\!{p[j]}' for j in range(3)) + '$', 'encre', 's')
save(fig, '44-207')
