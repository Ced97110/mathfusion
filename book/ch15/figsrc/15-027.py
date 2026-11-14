import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, a, b, c in [(44, r'$x \div y$', r'$x$', r'$1/y$'), (14, r'$12 \div 4$', r'$12$', r'$1/4$')]:
    box(ax, 4, y, 24, 11, 'fixe', label=a); text(ax, 33, y + 5.5, '=', 'varie', 'l')
    box(ax, 38, y, 16, 11, 'sujet', label=b); text(ax, 60, y + 5.5, r'$\times$', 'varie', 'l'); box(ax, 66, y, 18, 11, 'autre', label=c)
text(ax, 46, 38, 'facteur', 'sujet', 's'); text(ax, 75, 38, 'facteur', 'autre', 's')
text(ax, 44, 7, r'$12 \div 4 = 3$ et $12 \times 1/4 = 3$', 'resultat', 's')
save(fig, '15-027')
