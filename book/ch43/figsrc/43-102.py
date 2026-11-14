import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
xs = [14, 32, 50, 68]
text(ax, 44, 72, 'une bijection : n → 2n', 'resultat', 'm')
text(ax, 2, 64, 'les entiers', 'sujet', 's', ha='left')
text(ax, 2, 10, 'les pairs', 'autre', 's', ha='left')
for x, n in zip(xs, range(4)):
    disc(ax, x, 54, 4, 'sujet', label=str(n))
    disc(ax, x, 20, 4, 'autre', label=str(2 * n))
    arrow(ax, (x, 49.5), (x, 24.5), 'varie')
text(ax, 82, 54, '…', 'sujet', 'l'); text(ax, 82, 20, '…', 'autre', 'l')
save(fig, '43-102')
