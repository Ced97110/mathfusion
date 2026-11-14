import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'$b=\sigma(a_1)$ suivi de droite à gauche', 'encre', 'm')
xs = [10, 32, 54, 76]; labs = ['2', '1', '2', '1']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
below = [r'$b=\sigma(a_1)$', r'$a_1$', r'$a_2$', r'$\sigma(a_2)$']
for x, l, r, b in zip(xs, labs, roles, below):
    disc(ax, x, 30, 4.2, r, label=l, size='m'); text(ax, x, 21, b, r, 's')
for i, (n, lw, r) in enumerate([(r'$\sigma^{-1}$', 2.2, 'varie'), (r'$\tau$', 1.0, 'fixe'), (r'$\sigma$', 1.0, 'fixe')]):
    arrow(ax, (xs[i] + 4.8, 30), (xs[i + 1] - 4.8, 30), r, lw=lw)
    text(ax, (xs[i] + xs[i + 1]) / 2, 36, n, r, 'm')
text(ax, 21, 11, 'étape décisive', 'varie', 's')
text(ax, 66, 11, r'$\sigma(a_1)\to\sigma(a_2)$', 'resultat', 's')
save(fig, '47-170')
