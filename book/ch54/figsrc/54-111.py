import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
A = lambda t: 2 - t + 3 * t ** 3
B = lambda t: 1 + t
assert A(2) == 24 and B(2) == 3 and A(2) + B(2) == 27 == 3 + 3 * 2 ** 3
top = [(r'$2-x+3x^3$', 'sujet'), (r'$1+x$', 'autre'), (r'$3+3x^3$', 'resultat')]
bot = [('24', 'sujet'), ('3', 'autre'), ('27', 'resultat')]
xs = [3, 33, 63]
for i in range(3):
    box(ax, xs[i], 40, 22, 10, top[i][1], label=top[i][0], size='s')
    arrow(ax, (xs[i] + 11, 39.5), (xs[i] + 11, 21.5), 'varie')
    box(ax, xs[i], 11, 22, 10, bot[i][1], label=bot[i][0], size='m')
text(ax, 29, 45, '+', 'encre', 'l'); text(ax, 59, 45, '=', 'encre', 'l')
text(ax, 29, 16, '+', 'encre', 'l'); text(ax, 59, 16, '=', 'encre', 'l')
text(ax, 26, 30.5, r'$x\mapsto2$', 'varie', 's')
text(ax, 44, 4, '24 + 3 = 27 : même résultat', 'resultat', 's')
text(ax, 44, 56, 'additionner puis remplacer, ou l’inverse', 'encre', 's')
save(fig, '54-111')
