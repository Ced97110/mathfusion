import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'$f=x^3-3x+2$', 'sujet', 'l')
xs = [14, 34, 54, 74]
for x, p in zip(xs, [r'$x^3$', r'$x^2$', r'$x$', r'$1$']):
    text(ax, x, 53, p, 'fixe', 's')
for x, c in zip(xs, ['1', '0', '−3', '2']):
    box(ax, x - 8, 40, 16, 9, 'sujet', label=c)
vals = ['3', '0', '−3']
for k in range(3):
    x = xs[k + 1]
    box(ax, x - 8, 14, 16, 9, 'resultat', label=vals[k])
    arrow(ax, (xs[k], 39), (x, 24.5), 'varie')
text(ax, 44, 7, r"$f'=3x^2-3$", 'resultat', 'l')
save(fig, '62-042')
