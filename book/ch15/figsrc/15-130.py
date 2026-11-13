import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 22, 52, 44, 11, 'sujet', label=r'$0r + 0s = 0$', size='l')
for y, rv in ((30, '7'), (10, '100')):
    box(ax, 3, y, 22, 13, 'varie', label=r'$r$ = ' + rv)
    arrow(ax, (25, y + 6.5), (32, y + 6.5), 'fixe')
    text(ax, 49, y + 6.5, r'$0 \times$ ' + rv, 'sujet', 'm')
    arrow(ax, (64, y + 6.5), (70, y + 6.5), 'fixe')
    box(ax, 70, y, 15, 13, 'resultat', label='0', size='l')
text(ax, 44, 46, 'quelle que soit la valeur', 'varie', 's')
save(fig, '15-130')
