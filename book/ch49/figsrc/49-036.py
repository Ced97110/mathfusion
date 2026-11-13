import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 20, 68, 'lettre', 'sujet', 'm'); text(ax, 68, 68, r'élément de $M$', 'varie', 'm')
for i in range(2):
    y = 52 - i * 16
    box(ax, 10, y - 5, 20, 10, 'sujet', label=r'$x_%d$' % (i + 1))
    box(ax, 58, y - 5, 20, 10, 'varie', label=r'$a_%d$' % (i + 1))
    arrow(ax, (31, y), (57, y), 'varie')
    text(ax, 44, y + 3, r'$\mapsto$', 'varie', 'm')
text(ax, 44, 26, r'$x_i\mapsto a_i$ : « est envoyé sur »', 'varie', 'm')
box(ax, 10, 6, 20, 10, 'fixe', label=r'$FM$')
box(ax, 58, 6, 20, 10, 'fixe', label=r'$M$')
arrow(ax, (31, 11), (57, 11), 'fixe')
text(ax, 44, 15, r'$\to$ : ensembles', 'fixe', 's')
save(fig, '49-036')
