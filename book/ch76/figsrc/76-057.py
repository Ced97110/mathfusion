import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [2, 31, 60]; wd = 26
text(ax, 44, 51, 'trois produits de 3 vecteurs de base', 'fixe', 's') if False else None
box(ax, xs[0], 28, wd, 12, 'resultat', label=r'$e_1\wedge e_3$')
box(ax, xs[1], 28, wd, 12, 'varie', label=r'$e_3\wedge e_1$')
box(ax, xs[2], 28, wd, 12, 'limite', label=r'$e_2\wedge e_2$')
for x, t, r in zip(xs, ['numéros croissants', 'ordre cassé', 'numéro répété'], ['resultat', 'varie', 'limite']):
    text(ax, x + 13, 46, t, r, 's')
for x, t, r in zip(xs, ['monôme standard', r'$=-\,e_1\wedge e_3$', r'$=0$'], ['resultat', 'varie', 'limite']):
    arrow(ax, (x + 13, 27), (x + 13, 18), r)
    text(ax, x + 13, 12, t, r, 's')
save(fig, '76-057')
