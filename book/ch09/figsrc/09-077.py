import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [3, 33, 63]
for x, h in zip(xs, ['fraction', 'geste', 'pourcentage']):
    text(ax, x + 11, 61, h, 'fixe', 's')
rows = [(44, r'$\frac{3}{5}$', r'3 $\times$ 100 $\div$ 5', '60 %'), (26, r'$\frac{1}{3}$', r'1 $\times$ 100 $\div$ 3', r'$33\frac{1}{3}$ %'), (8, r'$\frac{3}{8}$', r'3 $\times$ 100 $\div$ 8', '37,5 %')]
for y, a, b, c in rows:
    box(ax, xs[0], y, 22, 12, 'sujet', label=a)
    box(ax, xs[1], y, 22, 12, 'varie', label=b, size='s')
    box(ax, xs[2], y, 22, 12, 'resultat', label=c)
    arrow(ax, (25.5, y + 6), (32, y + 6), 'varie')
    arrow(ax, (55.5, y + 6), (62, y + 6), 'varie')
save(fig, '09-077')
