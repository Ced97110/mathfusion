import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = [56, 67, 78]
text(ax, 3, 68, r'$n_2 = 3$ : trois 2-Sylow', 'sujet', 'm', ha='left')
for k, x in zip('ABC', X): disc(ax, x, 68, 4, 'sujet', label=r'$P_%s$' % k, size='s')
# condition 1 : divise q = 3
text(ax, 3, 46, r'$3 \mid q = 3$ : vrai', 'resultat', 'm', ha='left')
box(ax, 50, 40, 34, 12, 'resultat')
for x in X: disc(ax, x, 46, 3.2, 'sujet')
text(ax, 67, 35.5, r'$1 \times 3 = 3$', 'resultat', 's')
# condition 2 : 3 - 1 = 2 est pair
text(ax, 3, 22, r'$3 \equiv 1\ (\mathrm{mod}\ 2)$ : vrai', 'resultat', 'm', ha='left')
disc(ax, X[0], 22, 3.2, 'fixe')
box(ax, 61.5, 16, 22.5, 12, 'resultat')
for x in X[1:]: disc(ax, x, 22, 3.2, 'sujet')
text(ax, 67, 11.5, r'$3 - 1 = 2$ : pair', 'resultat', 's')
save(fig, '50-087')
