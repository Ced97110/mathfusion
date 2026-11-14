import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(98)
text(ax, 44, 92, r'$x^3-8=(x-2)(x^2+2x+4)$', 'encre', 'l')
text(ax, 44, 85, r'essai avec $x=3$', 'encre', 's')
# côté gauche : 27 cubes dont 8 retirés = 19
cells = [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if not (i <= 1 and j <= 1 and k >= 1)]
assert len(cells) == 19
cubes(ax, cells, (21, 34), 5.6, 'sujet', lw=0.4)
text(ax, 21, 76, r'$x^3-8$', 'sujet', 'm')
text(ax, 21, 23, r'$27-8=19$', 'sujet', 'm')
text(ax, 21, 17, '27 cubes, 8 retirés', 'sujet', 's')
text(ax, 43, 50, '=', 'resultat', 'xl')
# côté droit : les deux facteurs puis le produit
text(ax, 68, 76, r'$(x-2)(x^2+2x+4)$', 'encre', 's')
box(ax, 50, 57, 36, 11, 'varie', label=r'$x-2=1$', size='s')
box(ax, 54, 41, 32, 11, 'autre', label=r'$x^2+2x+4=9+6+4=19$', size='s')
arrow(ax, (51.5, 57), (51.5, 36.5), 'varie', lw=1.0)
arrow(ax, (74, 41), (74, 36.5), 'autre', lw=1.0)
box(ax, 50, 25, 36, 11, 'resultat', label=r'$1\times 19=19$', size='s')
text(ax, 44, 9.5, 'les deux côtés valent 19', 'resultat', 'm')
text(ax, 44, 3.5, 'un essai : ce n’est pas une preuve', 'fixe', 's')
save(fig, '39-118')
