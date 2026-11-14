import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = [14 + k * 15 for k in range(5)]
ya, yb = 64, 32
text(ax, 44, 73, r'cycle $(1\,2\,3)$ dans $K$', 'sujet', 's')
text(ax, 44, 23.5, r'cycle $(2\,4\,5)$ dans $K$', 'resultat', 's')
for k, x in enumerate(xs):
    disc(ax, x, ya, 3.6, 'sujet' if k < 3 else 'fixe', label=str(k + 1))
    disc(ax, x, yb, 3.6, 'resultat' if k in (1, 3, 4) else 'fixe', label=str(k + 1))
for i, j in ((0, 1), (1, 3), (2, 4)):
    arrow(ax, (xs[i], ya - 4.2), (xs[j], yb + 4.2), 'varie', lw=1.2)
text(ax, 44, 13, r'$\gamma=(1\,2\,4)(3\,5)$ impaire', 'limite', 's')
text(ax, 44, 6, r'suivie de $(1\,3)$ : paire', 'resultat', 's')
save(fig, '64-109')
