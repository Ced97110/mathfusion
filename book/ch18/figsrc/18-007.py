import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(55)
box(ax,6,38,22,10,'fixe',label=r'$6x$'); text(ax,33,43,'+','encre','l'); box(ax,38,38,16,10,'fixe',label='9')
box(ax,6,12,10,10,'sujet',label='3',weight='bold'); text(ax,19,17,r'$\times$','encre','m'); box(ax,22,12,16,10,'fixe',label=r'$2x$')
text(ax,44,17,'+','encre','l')
box(ax,50,12,10,10,'sujet',label='3',weight='bold'); text(ax,63,17,r'$\times$','encre','m'); box(ax,66,12,14,10,'fixe',label='3')
arrow(ax,(17,37),(17,23),'varie'); arrow(ax,(46,37),(62,23),'varie')
text(ax,44,5,'le facteur 3 est dans les deux','sujet','s')
save(fig,'18-007')
