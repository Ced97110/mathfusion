import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
xs = [10, 32, 54, 76]
comp = ['540', '270', '135', '27']
leaf = ['2', '2', '5', r'$3^3$']
for i, x in enumerate(xs):
    box(ax, x - 8, 54, 16, 9, 'sujet', label=comp[i])
    line(ax, [(x, 54), (x, 43)], 'fixe')
    box(ax, x - 6, 34, 12, 9, 'resultat', label=leaf[i], size='l')
    if i < 3:
        arrow(ax, (x + 8.5, 58.5), (xs[i + 1] - 8.5, 58.5), 'varie')
brace(ax, 4, 38, 31, 'resultat', label=r'$2^2$')
text(ax, 44, 11, r'$540=2^2\times3^3\times5$', 'encre', 'l', weight='bold')
save(fig, '60-235')
