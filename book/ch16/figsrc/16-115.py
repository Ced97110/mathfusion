import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 3, 30, 54, 14, 'sujet', label=r'$P = 2l + 2w$', size='l')
box(ax, 3, 6, 54, 14, 'autre', label=r'$l = (P - 2w)\,/\,2$', size='l')
box(ax, 60, 30, 25, 14, 'varie', label=r'cherche $P$')
box(ax, 60, 6, 25, 14, 'varie', label=r'cherche $l$')
arrow(ax, (30, 21), (30, 29), 'fixe', both=True)
text(ax, 44, 25, 'même relation', 'fixe', 's', ha='left')
save(fig, '16-115')
