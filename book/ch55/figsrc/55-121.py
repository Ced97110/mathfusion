import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
f = lambda x: (x ** 7 + 2 * x ** 2) % 5
f0 = lambda x: (x ** 3 + 2 * x ** 2) % 5
xs = [0, 1, 2, 3, 4]
assert [f(x) for x in xs] == [f0(x) for x in xs] == [0, 3, 1, 0, 1]
text(ax, 44, 76, r'sur $\mathbb{Z}/5\mathbb{Z}$', 'fixe', 'm')
# the division, piece by piece
text(ax, 44, 66, r'$x^7 \;=\; x^2\,(x^5-x) \;+\; x^3$', 'encre', 'l')
text(ax, 44, 58.5, r'$x^2\,(x^5-x)$ vaut 0 en chaque point', 'fixe', 's')
# the two polynomials: different degrees
box(ax, 4, 38, 38, 9, 'sujet', label=r'$f=x^7+2x^2$', size='m')
box(ax, 46, 38, 38, 9, 'autre', label=r'$f_0=x^3+2x^2$', size='m')
text(ax, 44, 51, r'degrés 7 et 3 : polynômes différents', 'encre', 's')
text(ax, 44, 33, 'mêmes valeurs aux 5 points', 'resultat', 's')
# the same values in the five points
text(ax, 8, 28, r'$x$', 'fixe', 's')
for j, x in enumerate(xs):
    cx = 22 + j * 12
    text(ax, cx + 5, 28, str(x), 'fixe', 's')
    box(ax, cx, 17, 10, 7, 'sujet', label=str(f(x)), size='m')
    box(ax, cx, 7, 10, 7, 'autre', label=str(f0(x)), size='m')
text(ax, 8, 20.5, r'$f$', 'sujet', 'm')
text(ax, 8, 10.5, r'$f_0$', 'autre', 'm')
save(fig, '55-121')
