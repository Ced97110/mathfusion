import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools
fig, ax = canvas(72)
D = lambda x1, x2, x3: (x1 - x2) * (x1 - x3) * (x2 - x3)
d0 = D(1, 2, 4)
assert d0 == -6
neg = lambda n: str(n).replace('-', '−')
plus = [p for p in itertools.permutations((1, 2, 4)) if D(*p) == d0]
minus = [p for p in itertools.permutations((1, 2, 4)) if D(*p) == -d0]
assert len(plus) == 3 and len(minus) == 3
text(ax, 22, 66, r'$+D$ : valeur $-6$', 'sujet', 'm', weight='bold')
text(ax, 66, 66, r'$-D$ : valeur $6$', 'varie', 'm', weight='bold')
for k, p in enumerate(plus):
    box(ax, 3, 48 - k * 14, 38, 9, 'sujet', label=f'{p[0]}, {p[1]}, {p[2]} : ' + neg(D(*p)), size='m')
for k, p in enumerate(minus):
    box(ax, 47, 48 - k * 14, 38, 9, 'varie', label=f'{p[0]}, {p[1]}, {p[2]} : ' + neg(D(*p)), size='m')
text(ax, 44, 5, r'chaque permutation donne $+D$ ou $-D$', 'encre', 's')
save(fig, '55-144')
