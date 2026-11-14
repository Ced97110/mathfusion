import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 4, 20, 48, 24, 'fixe', fill=False, dash=True)
text(ax, 28, 48, 'terme', 'autre', 'm')
box(ax, 9, 25, 12, 11, 'sujet', label=r'$5$'); text(ax, 28, 30.5, r'$\times$', 'varie', 'l'); box(ax, 35, 25, 12, 11, 'sujet', label=r'$2$')
text(ax, 58, 30.5, '+', 'varie', 'l'); box(ax, 66, 25, 14, 11, 'autre', label=r'$3$')
text(ax, 73, 48, 'terme', 'autre', 'm')
brace(ax, 9, 47, 22, 'sujet', 'facteurs', size='m')
save(fig, '15-022')
