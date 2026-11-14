import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
gy = 14
line(ax, [(2, gy), (86, gy)], 'fixe')
poly(ax, [(58, gy), (70, 40), (82, gy)], 'fixe')
xs = {'A': 10, 'B': 34, 'H': 70}
for k, x in xs.items():
    disc(ax, x, gy, 1.5, 'sujet' if k != 'H' else 'fixe')
    text(ax, x, gy - 5, '$%s$' % k, 'sujet' if k != 'H' else 'fixe', 'm')
arrow(ax, (xs['A'] + 3, gy + 6), (xs['B'] - 3, gy + 6), 'varie')
text(ax, 22, gy + 11, 'on avance', 'varie', 's')
text(ax, 44, 42, 'même droite horizontale', 'fixe', 's')
text(ax, 22, 5, '$B$ entre $A$ et $H$', 'sujet', 's')
save(fig, '38-013')
