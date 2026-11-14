import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
text(ax, 44, 60, r'$\nu$ : de $R$ vers $R/I$', 'encre', 's')
for n in range(4):
    x = 14 + n * 20
    disc(ax, x, 46, 5, 'sujet', label=str(n), size='m')
    box(ax, x - 8, 14, 16, 11, 'resultat', label=r'$%d+I$' % n, size='s')
    arrow(ax, (x, 40.5), (x, 26.5), 'varie')
text(ax, 4, 54, 'éléments', 'sujet', 's', ha='left'); text(ax, 4, 8, 'classes : toutes atteintes', 'resultat', 's', ha='left')
text(ax, 80, 33, r'$\nu$', 'varie', 'm')
save(fig, '52-144')
