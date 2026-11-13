import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# x^4 - 1 = (x-1)(x+1)(x^2+1) ; widths proportional to the degrees 1, 1, 2 ; value at x = 2 : 1 x 3 x 5 = 15
text(ax, 44, 77, r'$x^4-1$', 'sujet', 'l')
x0 = 6; u = 19.0
brace(ax, x0, x0 + 4 * u, 62, 'sujet', label='degré 4', down=False)
box(ax, x0, 40, u - 1, 12, 'fixe', label=r'$x-1$', size='s')
box(ax, x0 + u, 40, u - 1, 12, 'fixe', label=r'$x+1$', size='s')
box(ax, x0 + 2 * u, 40, 2 * u - 1, 12, 'varie', label=r'$x^2+1$')
text(ax, x0 + u, 34, 'déjà dans ℚ', 'fixe', 's')
text(ax, x0 + 3 * u, 34, 'un étage : ℚ($i$)', 'varie', 's')
text(ax, 44, 24, r'en $x=2$ : $1\times3\times5=15=2^4-1$', 'encre', 's')
box(ax, 8, 4, 72, 12, 'resultat', label=r'corps de décomposition : ℚ($i$)', size='s')
save(fig, '62-125')
