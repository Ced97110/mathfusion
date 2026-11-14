import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
coef = [1, 0, -6, 0, -27, -3]
assert all(c % 3 == 0 for c in coef[1:]) and coef[0] % 3 and coef[-1] % 9
text(ax, 44, 61, r'$f=x^5-6x^3-27x-3$', 'encre', 'm')
w, g = 12.5, 1.5
xs = [3 + i * (w + g) for i in range(6)]
for i, (x, c) in enumerate(zip(xs, coef)):
    box(ax, x, 30, w, 11, 'autre' if i == 0 else 'resultat', label=str(c).replace('-', '−'))
brace(ax, xs[1], xs[5] + w, 43, 'resultat', down=False, label=None)
text(ax, 55, 49, 'divisibles par 3', 'resultat', 's')
brace(ax, xs[0], xs[0] + w, 29, 'autre', down=True, label=None)
text(ax, 2, 20, 'pas divisible par 3', 'autre', 's', ha='left')
brace(ax, xs[5], xs[5] + w, 29, 'varie', down=True, label=None)
text(ax, 86, 20, r'pas par $9=3^2$', 'varie', 's', ha='right')
box(ax, 14, 3, 60, 9, 'resultat', label=r'Eisenstein, $p=3$ : $f$ irréductible', size='s')
save(fig, '64-175')
