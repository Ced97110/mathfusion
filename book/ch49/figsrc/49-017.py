import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
O = (12, 8); a, b = 30, 15
disc(ax, *O, 1.6, 'fixe')
text(ax, O[0] + 6, O[1] - 4, 'départ', 'fixe', 's')
# chemin x puis y
arrow(ax, (O[0] + 1.6, O[1]), (O[0] + a, O[1]), 'sujet')
arrow(ax, (O[0] + a, O[1]), (O[0] + a, O[1] + b - 2), 'sujet')
disc(ax, O[0] + a, O[1] + b, 2.0, 'sujet')
text(ax, O[0] + a / 2, O[1] - 3, r'$x$', 'sujet', 'm')
text(ax, O[0] + a + 3, O[1] + b / 2, r'$y$', 'sujet', 'm')
text(ax, O[0] + a + 5, O[1] + b + 4, r'$xy$', 'sujet', 'l')
# chemin y puis x
arrow(ax, (O[0], O[1] + 1.6), (O[0], O[1] + a), 'autre')
arrow(ax, (O[0], O[1] + a), (O[0] + b - 2, O[1] + a), 'autre')
disc(ax, O[0] + b, O[1] + a, 2.0, 'autre')
text(ax, O[0] - 3, O[1] + a / 2, r'$y$', 'autre', 'm')
text(ax, O[0] + b / 2, O[1] + a + 3, r'$x$', 'autre', 'm')
text(ax, O[0] + b + 6, O[1] + a + 4, r'$yx$', 'autre', 'l')
text(ax, 64, 48, r'$xy \neq yx$', 'limite', 'xl')
text(ax, 64, 41, 'deux points', 'encre', 's')
text(ax, 64, 37.5, 'différents', 'encre', 's')
save(fig, '49-017')
