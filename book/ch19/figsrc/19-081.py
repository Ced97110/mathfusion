import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 62, 60, 14, 'sujet', label=r'$2x+3y=12$', size='l')
box(ax, 14, 34, 60, 14, 'fixe', label=r'$3y=12-2x$', size='l')
box(ax, 14, 8, 60, 14, 'resultat', label=r'$y=4-\frac{2}{3}x$', size='l')
arrow(ax, (44, 61), (44, 49), 'varie'); text(ax, 48, 55, r'$-\,2x$ des deux côtés', 'varie', 's', ha='left')
arrow(ax, (44, 33), (44, 23), 'varie'); text(ax, 48, 27, r'÷ 3 des deux côtés', 'varie', 's', ha='left')
text(ax, 44, 3, r'$y$ seul : on s’arrête', 'resultat', 's')
save(fig, '19-081')
