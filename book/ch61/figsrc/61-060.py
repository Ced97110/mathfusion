import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 32, 36, 24, 14, 'sujet', label=r'$u$', size='xl')
text(ax, 44, 54, r'$u$ dans $E$', 'sujet', 's')
arrow(ax, (38, 35.5), (22, 24), 'varie'); arrow(ax, (50, 35.5), (66, 24), 'varie')
box(ax, 8, 12, 28, 11, 'varie', label=r'$u=\sqrt{2}$', size='m'); box(ax, 52, 12, 28, 11, 'varie', label=r'$u=i$', size='m')
text(ax, 44, 5, 'une lettre, plusieurs éléments', 'fixe', 's')
save(fig, '61-060')
