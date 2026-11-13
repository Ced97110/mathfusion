import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 24, 42, 27, 10, 'autre', label='$x$'); box(ax, 53, 42, 27, 10, 'autre', label='$3$')
box(ax, 6, 26, 16, 14, 'sujet', label='$x$'); box(ax, 6, 10, 16, 14, 'sujet', label='$2$')
pairs = [(r'$x \cdot x$', r'$x \cdot 3$'), (r'$2 \cdot x$', r'$2 \cdot 3$')]
for (y, pr) in ((26, pairs[0]), (10, pairs[1])):
    box(ax, 24, y, 27, 14, 'resultat', label=pr[0]); box(ax, 53, y, 27, 14, 'resultat', label=pr[1])
text(ax, 44, 4, r'$2 \times 2 = 4$ paires, 4 régions', 'resultat', 's')
save(fig, '15-095')
