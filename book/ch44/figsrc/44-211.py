import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(78)
eqs = [(r'$ab=ac$', 'sujet'), (r'$a^{-1}(ab)=a^{-1}(ac)$', 'varie'),
       (r'$(a^{-1}a)\,b=(a^{-1}a)\,c$', 'varie'), (r'$1\,b=1\,c$', 'varie'), (r'$b=c$', 'resultat')]
eqs = [eqs[0], eqs[1], eqs[2], eqs[4]]
side = [r'×$a^{-1}$ à gauche', 'on regroupe', r'$a^{-1}a=1$']
ys = [64, 46, 28, 10]; bx, bw, bh = 3, 52, 11
text(ax, 44, 76, 'dans un groupe', 'sujet', 's', weight='bold')
for i, (s, role) in enumerate(eqs):
    box(ax, bx, ys[i] - bh / 2, bw, bh, role if i in (0, 3) else 'fixe', label=s, size='m')
for i in range(3):
    arrow(ax, (bx + bw / 2, ys[i] - bh / 2 - .3), (bx + bw / 2, ys[i + 1] + bh / 2 + .3), 'varie', lw=1.1)
    text(ax, 71, (ys[i] + ys[i + 1]) / 2, side[i], 'varie', 's')
save(fig, '44-211')
