import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 22; u = s / 5; y0 = 12
xs = [2, 33, 64]
for k, x0 in enumerate(xs):
    m = lambda x, y, x0=x0: (x0 + (x + 1) * u, y0 + (y + 1) * u)
    if k == 0: poly(ax, [m(-1, -1), m(-1, 0), m(3, 4), m(4, 4), m(4, -1)], 'varie')
    if k == 1: poly(ax, [m(-1, -1), m(-1, 4), m(4, -1)], 'sujet')
    if k == 2: poly(ax, [m(-1, -1), m(-1, 0), m(1, 2), m(4, -1)], 'resultat')
    poly(ax, [m(-1, -1), m(4, -1), m(4, 4), m(-1, 4)], 'fixe', fill=False)
    line(ax, [m(-1, 0), m(3, 4)], 'varie' if k != 1 else 'fixe', lw=1.2)
    line(ax, [m(-1, 4), m(4, -1)], 'sujet' if k != 0 else 'fixe', lw=1.2)
text(ax, xs[0] + s / 2, y0 + s + 5, r'$y\leq x+1$', 'varie', 's')
text(ax, xs[1] + s / 2, y0 + s + 5, r'$x+y\leq 3$', 'sujet', 's')
text(ax, xs[2] + s / 2, y0 + s + 5, 'zone commune', 'resultat', 's')
text(ax, (xs[0] + s + xs[1]) / 2, y0 + s / 2, 'et', 'encre', 'm')
text(ax, (xs[1] + s + xs[2]) / 2, y0 + s / 2, '=', 'encre', 'l')
text(ax, xs[0] + s / 2, y0 - 5, 'un demi-plan', 'varie', 's')
text(ax, xs[1] + s / 2, y0 - 5, 'un autre', 'sujet', 's')
text(ax, xs[2] + s / 2, y0 - 5, 'dans les deux', 'resultat', 's')
save(fig, '20-102')
