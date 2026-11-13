import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 24, 46, 40, 9, 'fixe', label='« le polynôme »')
arrow(ax, (34, 46), (22, 41), 'fixe')
arrow(ax, (54, 46), (66, 41), 'fixe')
text(ax, 22, 38, 'liste de coefficients', 'sujet', 's')
text(ax, 66, 38, 'table de valeurs', 'autre', 's')
for i, c in enumerate([r'$0$', r'$-1$', r'$0$', r'$1$']):
    box(ax, 4 + 10 * i, 18, 9, 12, 'sujet', label=c)
box(ax, 48, 24, 36, 11, 'autre', label=r'$2\mapsto 6$')
box(ax, 48, 9, 36, 11, 'autre', label=r'$3\mapsto 24$')
save(fig, '55-002')
