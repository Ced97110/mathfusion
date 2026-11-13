import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 3, 10, 82, 40, 'sujet', r=3)
text(ax, 44, 44, 'un seul bloc : même valeur', 'sujet', 's')
for x, (n, d) in ((18, (6, 8)), (44, (3, 4)), (70, (9, 12))):
    text(ax, x, 26, rf'$\frac{{{n}}}{{{d}}}$', 'sujet', 'l')
arrow(ax, (24, 26), (38, 26), 'varie'); text(ax, 31, 33, r'$\div 2$', 'varie', 's')
arrow(ax, (50, 26), (63, 26), 'varie'); text(ax, 56.5, 33, r'$\times 3$', 'varie', 's')
text(ax, 44, 15, 'autre écriture, même bloc', 'fixe', 's')
save(fig, '43-032')
