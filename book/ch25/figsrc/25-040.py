import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(68)
u=40; ox,oy=8,8
P=lambda x,y:(ox+x*u,oy+y*u)
arrow(ax,(ox,oy),(ox+62,oy),'fixe')
line(ax,[P(0,0),P(1.25,0.75*1.25)],'sujet',lw=1.4)
line(ax,[P(0,0),P(1.25,0.4*1.25)],'fixe',dash=True); line(ax,[P(0,0),P(1.15,1.2*1.15)],'fixe',dash=True)
line(ax,[P(1,0),P(1,1.2)],'fixe',dash=True); line(ax,[P(1,0),P(1,0.75)],'varie',lw=1.8)
disc(ax,*P(1,0.75),1.2,'resultat')
ax.add_patch(Arc((ox,oy),20,20,theta1=0,theta2=37,color=COL['sujet'],lw=0.8))
text(ax,ox+u/2,oy-3.5,'1','fixe','s'); text(ax,ox+u+9,oy+12,'r = 0,75','varie','s')
text(ax,ox+u+9,oy+0.75*u-7,'(1, r)','resultat','s')
text(ax,ox+u+6,oy-3.5,'','fixe','s')
text(ax,70,40,'un seul angle','sujet','s'); text(ax,70,34,'pour ce rapport','sujet','s')
text(ax,18,60,'autre angle, autre hauteur','fixe','s')
save(fig,'25-040')
