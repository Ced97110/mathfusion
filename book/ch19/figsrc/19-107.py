import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 22, 70, 'avec A(1, 1)', 'sujet', 'm', weight='bold'); text(ax, 66, 70, 'avec B(4, 3)', 'autre', 'm', weight='bold')
box(ax, 2, 46, 40, 13, 'sujet', label=r'$y-1=\frac{2}{3}(x-1)$', size='s')
box(ax, 46, 46, 40, 13, 'autre', label=r'$y-3=\frac{2}{3}(x-4)$', size='s')
arrow(ax, (22, 46), (36, 34), 'varie'); arrow(ax, (66, 46), (52, 34), 'varie')
box(ax, 14, 20, 60, 13, 'resultat', label=r'$y=\frac{2}{3}x+\frac{1}{3}$', size='l')
text(ax, 44, 10, 'même équation : celle de la droite', 'resultat', 's')
save(fig, '19-107')
