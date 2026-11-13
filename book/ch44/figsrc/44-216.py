import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(64)
box(ax, 3, 36, 33, 22, 'autre'); box(ax, 52, 36, 33, 22, 'sujet')
text(ax, 19.5, 52, r'$S_3$', 'autre', 'xl', weight='bold'); text(ax, 68.5, 52, r'$D_3$', 'sujet', 'xl', weight='bold')
text(ax, 19.5, 42, 'rangements de 1, 2, 3', 'autre', 's'); text(ax, 68.5, 42, 'mouvements du triangle', 'sujet', 's')
text(ax, 44, 47, '=', 'resultat', 'xl', weight='bold')
box(ax, 22, 3, 44, 20, 'fixe')
for i in range(6): disc(ax, 28.5 + i * 6.2, 16, 2.4, 'resultat')
text(ax, 44, 8.5, 'un seul groupe de 6', 'encre', 's')
arrow(ax, (19.5, 35.6), (31, 23.4), 'resultat'); arrow(ax, (68.5, 35.6), (57, 23.4), 'resultat')
save(fig, '44-216')
