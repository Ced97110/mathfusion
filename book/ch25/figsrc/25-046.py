import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(58)
u=34; A=(8,8); C=(8+u,8); B=(8+u,8+u*math.tan(math.radians(40)))
ax.add_patch(Arc(A,2*u,2*u,theta1=0,theta2=90,color=COL['fixe'],lw=0.9))
line(ax,[(C[0],8),(C[0],50)],'fixe',dash=True)
line(ax,[A,B],'encre',lw=1.2); line(ax,[A,C],'sujet',lw=1.8); line(ax,[C,B],'varie',lw=2.2)
disc(ax,*C,1.0,'sujet'); disc(ax,*B,1.0,'varie')
ax.add_patch(Arc(A,16,16,theta1=0,theta2=40,color=COL['encre'],lw=0.9))
text(ax,4,9,'A','encre','s'); text(ax,C[0]+3,5,'C','sujet','s'); text(ax,B[0]-3,B[1]+3.5,'B','varie','s')
text(ax,25,3.5,'AC = 1','sujet','s'); text(ax,C[0]+3,22,'CB = tan A','varie','s',ha='left')
text(ax,26,47,'cercle de rayon 1','fixe','s'); text(ax,68,47,'droite tangente','fixe','s')
save(fig,'25-046')
