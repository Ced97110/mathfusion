import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
fig, ax = canvas(64)
def panel(x0, key, title, rolefn, arrowrole):
    text(ax, x0 + 17, 58, title, arrowrole, 's', weight='bold')
    p = P[key]; xs = [x0 + 5, x0 + 17, x0 + 29]
    for j in range(3):
        fixed = p[j] == j + 1
        role = rolefn(fixed)
        disc(ax, xs[j], 42, 3.4, role, label=str(j + 1))
        disc(ax, xs[j], 12, 3.4, role, label=str(j + 1))
        a = (xs[j], 42 - 4); b = (xs[p[j] - 1], 12 + 4)
        arrow(ax, a, b, 'fixe' if fixed else arrowrole, lw=1.1)
panel(2, 'a', r'$\tau_1$ : échange 2 et 3', lambda f: 'fixe' if f else 'varie', 'varie')
panel(48, 's', r'$\sigma$ : déplace les trois', lambda f: 'limite', 'limite')
save(fig, '44-208')
