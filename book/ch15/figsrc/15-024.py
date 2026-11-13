import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 30, 44, 28, 12, 'sujet', label=r'$5x$'); text(ax, 14, 50, 'terme', 'sujet', 'm')
arrow(ax, (38, 43), (24, 31), 'fixe'); arrow(ax, (50, 43), (64, 31), 'fixe')
box(ax, 14, 20, 20, 11, 'fixe', label=r'$5$'); box(ax, 54, 20, 20, 11, 'varie', label=r'$x$')
text(ax, 24, 14, 'facteur', 'fixe', 'm'); text(ax, 64, 14, 'facteur', 'varie', 'm')
text(ax, 24, 8, 'ne change pas', 'fixe', 's'); text(ax, 64, 8, 'change', 'varie', 's')
text(ax, 44, 25.5, r'$\times$', 'encre', 'l')
save(fig, '15-024')
