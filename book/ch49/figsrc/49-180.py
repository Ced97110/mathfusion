import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [10 + 17 * i for i in range(5)]; y = 34
box(ax, xs[1] - 7.5, y - 8, 17 * 3 + 15, 16, 'sujet', fill=True)
for i, x in enumerate(xs):
    disc(ax, x, y, 4.2, 'fixe' if i == 0 else 'sujet', label=str(i), size='l')
for i in range(1, 4):
    arrow(ax, (xs[i] + 4.6, y), (xs[i + 1] - 4.6, y), 'varie', lw=0.9)
text(ax, (xs[1] + xs[4]) / 2, y + 12, 'orbite de 1 : 4 points', 'sujet', 's')
text(ax, (xs[1] + xs[4]) / 2, y - 12, 'flèche : ajouter 1 (plafond 4)', 'varie', 's')
brace(ax, xs[0] - 5, xs[4] + 5, 17, 'fixe', 'monoïde : 5 éléments', depth=2.4)
text(ax, W / 2, 5, '4 ne divise pas 5', 'limite', 'l', weight='bold')
save(fig, '49-180')
