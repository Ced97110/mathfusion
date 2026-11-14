import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(50)
poly(ax,[(4,10),(40,10),(52,34),(16,34)],'sujet',lw=1.0)
disc(ax,28,22,1.5,'encre')
text(ax,28,16,'origine','encre','s')
text(ax,28,40,'plan, dimension 2','sujet','s')
arrow(ax,(54,22),(62,22),'varie')
text(ax,58,26,'on dit','varie','s')
box(ax,63,17,22,10,'resultat',label='« droite »',size='m')
save(fig,'80-086')
