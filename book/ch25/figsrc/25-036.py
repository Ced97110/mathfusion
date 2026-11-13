import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(62)
u=4.5; ox,oy=10,10
P=lambda x,y:(ox+x*u,oy+y*u)
arrow(ax,(ox,oy),(ox+60,oy),'fixe'); arrow(ax,(ox,oy),(ox,oy+48),'fixe')
line(ax,[P(0,0),P(11,8.25)],'encre',lw=1.2)
for (x,y) in ((4,3),(10,7.5)):
    line(ax,[P(x,0),P(x,y)],'fixe',dash=True); line(ax,[P(0,y),P(x,y)],'fixe',dash=True)
disc(ax,*P(4,3),1.1,'varie'); disc(ax,*P(10,7.5),1.1,'resultat')
text(ax,ox+4*u,oy-3,'4','varie','s'); text(ax,ox-3,oy+3*u,'3','varie','s')
text(ax,ox+10*u,oy-3,'4k','resultat','s'); text(ax,ox-4,oy+7.5*u,'3k','resultat','s')
text(ax,40,17,'(4, 3)','varie','s'); text(ax,67,38,'(4k, 3k)','resultat','s')
text(ax,70,26,'3k/4k = 3/4','resultat','s'); text(ax,70,20,'on simplifie par k','fixe','s'); text(ax,70,54,'k = 2,5','varie','s')
save(fig,'25-036')
