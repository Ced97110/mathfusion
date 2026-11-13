import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(62)
u=6; ox,oy=10,10
P=lambda x,y:(ox+x*u,oy+y*u)
arrow(ax,(ox,oy),(ox+62,oy),'fixe'); arrow(ax,(ox,oy),(ox,oy+46),'fixe')
line(ax,[P(0,0),P(9,6.75)],'encre',lw=1.2)
line(ax,[P(4,0),P(4,3)],'fixe',dash=True); line(ax,[P(8,0),P(8,6)],'fixe',dash=True)
line(ax,[P(0,3),P(4,3)],'fixe',dash=True); line(ax,[P(0,6),P(8,6)],'fixe',dash=True)
disc(ax,*P(4,3),1.1,'varie'); disc(ax,*P(8,6),1.1,'resultat')
for v in (4,8): text(ax,ox+v*u,oy-3,str(v),'fixe','s')
for v in (3,6): text(ax,ox-3,oy+v*u,str(v),'fixe','s')
text(ax,8,5,'(0, 0)','fixe','s'); text(ax,47,21,'(4, 3)','varie','s'); text(ax,73,40,'(8, 6)','resultat','s')
text(ax,24,44,'pente 3/4','encre','s'); text(ax,72,22,'6/8 = 3/4','resultat','s'); text(ax,72,16,'8 × 3/4 = 6','resultat','s')
save(fig,'25-035')
