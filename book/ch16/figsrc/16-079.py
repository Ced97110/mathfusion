import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 8, 16, 72, 44, 'varie')
text(ax, 44, 54, '− 7 : dernière opération', 'varie', 'm')
box(ax, 16, 20, 56, 28, 'sujet')
text(ax, 30, 34, r'$4\times$', 'sujet', 'l')
box(ax, 42, 25, 24, 18, 'fixe', label=r'$x$', size='l')
text(ax, 44, 8, '1er geste : défaire − 7', 'varie', 'm')
save(fig, '16-079')
