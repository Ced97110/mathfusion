import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [30 + 15 * i for i in range(4)]; top = [1, 2, 3, 4]; bot = [4, 3, 2, 1]
text(ax, 2, 46, 'numéros', 'fixe', 's', ha='left'); text(ax, 2, 24, 'images', 'fixe', 's', ha='left')
text(ax, 2, 35, r'$s$ =', 'sujet', 'l', ha='left')
for x, a, b in zip(xs, top, bot):
    disc(ax, x, 46, 4.5, 'sujet', label=str(a)); disc(ax, x, 24, 4.5, 'resultat', label=str(b))
    arrow(ax, (x, 41.2), (x, 28.8), 'varie')
text(ax, 38, 11, 'échange 1 et 4', 'varie', 's'); text(ax, 70, 11, 'échange 2 et 3', 'varie', 's')
save(fig, '44-034')
