import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
y = 62
box(ax, 8, y, 26, 10, 'sujet', label=r'$2x+3$')
box(ax, 54, y, 26, 10, 'autre', label=r'$3x+5$')
text(ax, 44, y + 5, r'$\times$', 'encre', 'l')
text(ax, 21, y - 4.5, 'contenu 1', 'sujet', 's')
text(ax, 67, y - 4.5, 'contenu 1', 'autre', 's')
arrow(ax, (44, y - 9), (44, 46), 'varie', lw=1.2)
y2 = 32
xs = [8, 34, 60]
for x, lab, role in zip(xs, [r'$6x^2$', r'$19x$', r'$15$'], ['fixe', 'resultat', 'fixe']):
    box(ax, x, y2, 20, 10, role, label=lab)
text(ax, 18, y2 - 5, 'diviseurs : 2, 3', 'fixe', 's')
text(ax, 70, y2 - 5, 'diviseurs : 3, 5', 'fixe', 's')
text(ax, 44, y2 - 11, 'ni 2, ni 3, ni 5 ne divise 19', 'resultat', 's')
text(ax, 44, 8, 'le produit est primitif : contenu 1', 'resultat', 's')
save(fig, '56-146')
