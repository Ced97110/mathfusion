import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
text(ax, 17, 55, '1er', 'fixe', 's'); text(ax, 40, 55, '2e', 'fixe', 's')
box(ax, 4, 34, 22, 14, 'sujet', label=r'$x=(3,1)$', size='s')
box(ax, 28, 34, 22, 14, 'autre', label=r'$y=(1,2)$', size='s')
box(ax, 4, 10, 22, 14, 'autre', label=r'$y=(1,2)$', size='s')
box(ax, 28, 10, 22, 14, 'sujet', label=r'$x=(3,1)$', size='s')
arrow(ax, (51, 41), (58, 41), 'fixe'); arrow(ax, (51, 17), (58, 17), 'fixe')
text(ax, 72, 41, r'$B(x,y)=5$', 'resultat', 'm'); text(ax, 72, 17, r'$B(y,x)=-5$', 'varie', 'm')
save(fig, '71-133')
