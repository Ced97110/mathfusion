import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 3, 54, 22, 12, 'sujet', label=r'$z_1=-5-w$', size='s')
box(ax, 33, 54, 22, 12, 'autre', label=r'$z_2=-4+w$', size='s')
box(ax, 63, 54, 22, 12, 'fixe', label=r'$y_1+y_2+y_3=0$', size='s')
text(ax, 29, 60, '+', 'encre', 'l')
text(ax, 59, 60, '+', 'encre', 'l')
box(ax, 10, 30, 68, 12, 'varie', label=r'$z_1+z_2+0=-9=3y_1$', size='m')
for x in (14, 44, 74):
    arrow(ax, (x, 54), (x if x == 44 else (24 if x == 14 else 64), 42.5), 'varie')
arrow(ax, (44, 30), (44, 19), 'varie')
text(ax, 47, 24.5, r'$\div 3$', 'varie', 's', ha='left')
box(ax, 24, 6, 40, 13, 'resultat', label=r'$y_1=-3$', size='m')
save(fig, '65-120')
