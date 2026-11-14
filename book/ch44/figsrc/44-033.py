import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [30 + 15 * i for i in range(4)]; top = [1, 2, 3, 4]; bot = [2, 3, 4, 1]
text(ax, 2, 46, 'numéros', 'fixe', 's', ha='left'); text(ax, 2, 22, 'images', 'fixe', 's', ha='left')
text(ax, 2, 34, r'$r$ =', 'sujet', 'l', ha='left')
for x, a, b in zip(xs, top, bot):
    disc(ax, x, 46, 4.5, 'sujet', label=str(a)); disc(ax, x, 22, 4.5, 'resultat', label=str(b))
    arrow(ax, (x, 41.2), (x, 26.8), 'varie')
text(ax, xs[0], 10, r'$r(1) = 2$', 'resultat', 's'); text(ax, xs[3], 10, r'$r(4) = 1$', 'resultat', 's')
save(fig, '44-033')
