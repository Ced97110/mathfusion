import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
text(ax,44,39,r'$x=5$','sujet','l')
box(ax,2,18,18,12,role='sujet',label='5'); arrow(ax,(22,24),(34,24),'varie'); text(ax,28,28,'carré','varie','s')
box(ax,36,18,16,12,role='sujet',label='25'); arrow(ax,(54,24),(68,24),'varie'); text(ax,61,28,'racine','varie','s')
box(ax,70,18,16,12,role='resultat',label='5')
text(ax,44,8,r'on retrouve $x$','resultat','m')
save(fig,'22-051')
