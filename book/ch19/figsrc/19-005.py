import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$y = 2x + 1$', 'encre', 'xl')
for y, a, b, c in [(26, r'$x$', r'$2x$', r'$y$'), (6, '3', '6', '7')]:
    box(ax, 3, y, 16, 12, 'sujet', label=a, size='l')
    box(ax, 36, y, 16, 12, 'fixe', label=b, size='l')
    box(ax, 69, y, 16, 12, 'resultat', label=c, size='l')
    arrow(ax, (20, y + 6), (35, y + 6), 'varie'); text(ax, 27.5, y + 9.5, r'$\times$ 2', 'varie', 's')
    arrow(ax, (53, y + 6), (68, y + 6), 'varie'); text(ax, 60.5, y + 9.5, '+ 1', 'varie', 's')
save(fig, '19-005')
