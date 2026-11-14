import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(88)
X = lambda x: 44 + x * 12.0
Y = lambda y: 34 + y * 3.6
xs = [-2.4 + i * 0.05 for i in range(97)]
f1 = lambda x: x**3 - 3 * x + 1
f2 = lambda x: x**3 - 3 * x + 3
line(ax, [(X(-2.5), 34), (X(2.5), 34)], 'fixe')
line(ax, [(X(x), Y(f1(x))) for x in xs], 'sujet', lw=1.3)
line(ax, [(X(x), Y(f2(x))) for x in xs], 'autre', lw=1.3)
for p, role in ((f1, 'resultat'), (f2, 'resultat')):
    for r in np.roots([1, 0, -3, p(0)]):
        if abs(r.imag) < 1e-9:
            disc(ax, X(r.real), 34, 1.3, role)
for x, y, role in ((-1, 3, 'sujet'), (1, -1, 'sujet'), (-1, 5, 'autre'), (1, 1, 'autre')):
    disc(ax, X(x), Y(y), 0.9, role)
    text(ax, X(x) + (-3 if x < 0 else 3.2), Y(y) + (1.5 if y > 0 else -1.5), f'{y}'.replace('-', '−'), role, 's')
text(ax, X(-1), 26, '−1', 'fixe', 's')
text(ax, X(1), 26, '1', 'fixe', 's')
text(ax, 6, 80, r'$x^3-3x+1$ : $d = 81 > 0$', 'sujet', 's', ha='left')
text(ax, 6, 74, r'$x^3-3x+3$ : $d = -135 < 0$', 'autre', 's', ha='left')
disc(ax, 60, 14, 1.3, 'resultat')
text(ax, 63, 14, 'racine réelle', 'resultat', 's', ha='left')
save(fig, '65-073')
