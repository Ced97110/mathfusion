import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
x0 = 44 - (12 * 6 + 11 * 1) / 2
for i in range(12): box(ax, x0 + 7 * i, 14, 6, 7, 'sujet', label=r'$z$', size='s')
text(ax, 44, 37, r'$z^{12}$', 'sujet', 'xl', weight='bold')
arrow(ax, (44, 32), (44, 23), 'varie')
brace(ax, x0, x0 + 83, 12, 'sujet', label=r'12 facteurs égaux à $z$')
save(fig, '66-022')
