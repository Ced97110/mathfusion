import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for x, s, n, r in [(6, r'$P$', '3e', 'autre'), (32, r'$A$', '2e', 'sujet'), (58, r'$P^{-1}$', '1er', 'autre')]:
    box(ax, x, 18, 24, 12, r, label=s, size='l'); text(ax, x + 12, 35, n, 'varie', 'm', weight='bold')
arrow(ax, (82, 13), (6, 13), 'varie', lw=1.3)
text(ax, 44, 6, 'on lit de droite à gauche', 'varie', 's')
save(fig, '43-046')
