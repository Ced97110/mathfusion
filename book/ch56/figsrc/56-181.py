import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'$x^3+2x+2$ irréductible sur $\mathbb{Q}$', 'resultat', 'm')
xs = [14, 34, 54, 74]
for x, h in zip(xs, [r'$x^3$', r'$x^2$', r'$x$', 'constante']):
    text(ax, x, 42, h, 'fixe', 's')
for x, c in zip(xs, ['1', '0', '2', '2']):
    box(ax, x - 8, 27, 16, 10, 'sujet', label=c)
for x, c in zip(xs, [r'$2\nmid1$', r'$2\mid0$', r'$2\mid2$', r'$2\mid2$']):
    text(ax, x, 20, c, 'resultat', 'm')
text(ax, 74, 11, r'$4\nmid2$', 'resultat', 'm')
save(fig, '56-181')
