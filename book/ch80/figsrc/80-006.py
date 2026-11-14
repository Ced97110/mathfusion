import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
disc(ax,32,34,19,'sujet',fill=False,lw=1.1); disc(ax,54,34,19,'autre',fill=False,lw=1.1)
text(ax,23,34,'multiples\nde 2','sujet','m'); text(ax,63,34,'multiples\nde 3','autre','m')
box(ax,38,30,10,8,'varie',label='6')
text(ax,43,8,'retiré 2 fois, remis 1 fois','varie','m')
arrow(ax,(43,11.5),(43,29),'varie')
save(fig,'80-006')
