import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'$I$ : terme constant pair', 'sujet', 'm')
items = [(6, 34, r'$x$', 'constant 0 : pair', 'resultat'), (52, 34, '2', 'constant 2 : pair', 'resultat'),
         (6, 8, r'$x+3$', 'constant 3 : impair', 'limite'), (52, 8, r'$2x+6$', 'constant 6 : pair', 'resultat')]
for x, y, p, c, role in items:
    box(ax, x, y, 30, 16, role)
    text(ax, x + 15, y + 11, p, role, 'l'); text(ax, x + 15, y + 4.5, c, role, 's')
arrow(ax, (37, 16), (51, 16), 'varie'); text(ax, 44, 20, r'$\times 2$', 'varie', 's')
text(ax, 22, 54, r'dans $I$', 'resultat', 's'); text(ax, 22, 29, r'hors $I$', 'limite', 's')
save(fig, '52-293')
