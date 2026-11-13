import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 78, 'modulo 5', 'autre', 'm')
text(ax, 66, 78, r'modulo $x^2+1$', 'sujet', 'm')
box(ax, 2, 22, 40, 52, 'autre')
box(ax, 46, 22, 40, 52, 'sujet')
for y, a, b, ra, rb in [(56, '2', r'$x$', 'resultat', 'resultat'),
                        (42, '7', r'$x^2+x+1$', 'fixe', 'fixe'),
                        (28, r'$-3$', r'$x^3+2x$', 'fixe', 'fixe')]:
    box(ax, 8, y, 28, 10, ra, label=a)
    box(ax, 50, y, 32, 10, rb, label=b)
text(ax, 22, 16, 'écarts multiples de 5', 'autre', 's')
text(ax, 66, 16, r'écarts multiples de $x^2+1$', 'sujet', 's')
text(ax, 44, 7, 'vert : le reste de la classe', 'resultat', 's')
save(fig, '54-196')
