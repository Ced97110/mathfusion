import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from itertools import combinations

R = [2, 3, 5]
a1 = sum(R); a2 = sum(x * y for x, y in combinations(R, 2)); a3 = R[0] * R[1] * R[2]
assert (a1, a2, a3) == (10, 31, 30)
fig, ax = canvas(74)
text(ax, 44, 69, 'racines 2, 3 et 5', 'fixe', 's')
cw, x0 = 19.0, 3.7
sym = [r'$x^3$', r'$-a_1x^2$', r'$+a_2x$', r'$-a_3$']
num = [r'$x^3$', r'$-10x^2$', r'$+31x$', r'$-30$']
how = ['', '2+3+5', '6+10+15', '2×3×5']
for k in range(4):
    x = x0 + k * (cw + 1.5)
    role = 'fixe' if k == 0 else 'sujet'
    box(ax, x, 48, cw, 11, role, label=sym[k], size='s')
    arrow(ax, (x + cw / 2, 47.5), (x + cw / 2, 40.5), 'varie', lw=0.9)
    box(ax, x, 29, cw, 11, role, label=num[k], size='s', weight='bold')
    if how[k]:
        text(ax, x + cw / 2, 22, how[k], 'varie', 's')
text(ax, 44, 12, 'a₁, a₂, a₃ : sans signe moins', 'resultat', 's')
text(ax, 44, 5.5, 'le moins est écrit dans le polynôme', 'resultat', 's')
save(fig, '65-049')
