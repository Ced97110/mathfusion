import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'le dénominateur', 'encre', 'm')
text(ax, 22, 40, '120', 'fixe', 'l'); line(ax, [(14, 35), (30, 35)], 'fixe', lw=1.2); box(ax, 15, 22, 14, 10, 'fixe', label='40', size='l')
text(ax, 66, 40, '120', 'sujet', 'l'); line(ax, [(58, 35), (74, 35)], 'sujet', lw=1.2); box(ax, 59, 22, 14, 10, 'varie', label=r'$v$', size='l')
text(ax, 22, 13, 'connu avant le calcul', 'fixe', 's'); text(ax, 66, 13, 'on ne sait pas encore', 'varie', 's')
text(ax, 44, 35, 'ou', 'encre', 's')
save(fig, '21-003')
