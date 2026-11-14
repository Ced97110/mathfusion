import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
E = [(1, 0), (0, 1), (1, 1)]
N = ['1', r'$\alpha$', r'$\alpha+1$']
def mul(p, q):
    a, b = p; c, d = q
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)
text(ax, 20, 75, r'$\mathbb{F}_4$ sans le 0', 'sujet', 'm')
x0, c = 2, 11
for j in range(3):
    text(ax, x0 + 9 + c * j + c / 2, 66, N[j], 'sujet', 's')
for i in range(3):
    yb = 52 - 11 * i
    text(ax, x0 + 4.5, yb + c / 2, N[i], 'sujet', 's')
    for j in range(3):
        r = mul(E[i], E[j]); v = (N + [None])[[(1, 0), (0, 1), (1, 1)].index(r)]
        box(ax, x0 + 9 + c * j, yb, c, c, 'resultat' if r == (1, 0) else 'fixe', label=v, size='s', r=0.4, lw=0.5)
text(ax, 20, 12, 'chaque ligne a un 1', 'resultat', 's')
text(ax, 66, 75, r'$\mathbb{Z}/4\mathbb{Z}$ : ligne du 2', 'limite', 'm')
for j in range(4):
    text(ax, 52 + 8.5 * j + 4.25, 66, str(j), 'fixe', 's')
    box(ax, 52 + 8.5 * j, 52, 8.5, 11, 'fixe', label=str(2 * j % 4), size='s', r=0.4, lw=0.5)
text(ax, 47, 57.5, '2×', 'encre', 's')
text(ax, 68, 40, 'aucun 1', 'limite', 'm')
text(ax, 68, 12, 'le test échoue', 'limite', 's')
save(fig, '67-018')
