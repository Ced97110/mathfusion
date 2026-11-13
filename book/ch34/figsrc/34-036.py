import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(64)
s=2.9
# left : two pieces
ox,oy=3,12
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+2.6*s,oy+3.5*s,'30','sujet','m');text(ax,ox+8*s,oy+3.5*s,'54','varie','m')
text(ax,ox+7*s,oy-4,r'$30+54=84$','resultat','m',weight='bold')
text(ax,ox+7*s,oy+12*s+9,'1re façon : 2 morceaux','encre','s')
# right : base QP
qx,qy=47,12
u=(13*s,0); Rr=(qx+7.615*s,qy+12.923*s); Pp=(qx+13*s,qy); Qq=(qx,qy)
poly(ax,[Qq,Pp,Rr],'fixe')
Hh=(Rr[0],qy)
line(ax,[Rr,Hh],'varie',lw=1.2,dash=True)
text(ax,Rr[0]+3.5,qy+6*s,'RH ?','varie','m',weight='bold')
text(ax,qx+6.5*s,qy-4,r'$\frac{1}{2}\times13\times RH=84$','resultat','s')
text(ax,qx+6.5*s,qy+12*s+9,'2e façon : base QP = 13','encre','s')
text(ax,qx-1,qy-3.2,'Q','fixe','s');text(ax,Pp[0]+1,qy-3.2,'P','fixe','s');text(ax,Rr[0],Rr[1]+2.5,'R','fixe','s')
save(fig,'34-036')
