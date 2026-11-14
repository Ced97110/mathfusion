import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
s=3.3
qx,qy=5,28
Qq=(qx,qy);Pp=(qx+13*s,qy);Rr=(qx+7.615*s,qy+12.923*s);Hh=(Rr[0],qy)
poly(ax,[Qq,Pp,Rr],'fixe')
line(ax,[Qq,Pp],'sujet',lw=1.8)
line(ax,[Rr,Hh],'varie',lw=1.4,dash=True)
brace(ax,qx,qx+13*s,qy-1,'sujet',label=r'$QP=r=13$')
text(ax,Hh[0]+4,qy+6*s,r'$RH$','varie','m',weight='bold')
text(ax,qx-2,qy-3,'Q','fixe','s');text(ax,Pp[0]+2,qy-3,'P','fixe','s');text(ax,Rr[0],Rr[1]+3,'R','fixe','s');text(ax,Hh[0]+2,qy+2.2,'H','fixe','s')
text(ax,qx+22,qy+3,r'$A+B$','fixe','s') if False else None
text(ax,44,14,r'$RH=p\,\sin(A+B)$','varie','m')
text(ax,44,7,r'$\mathrm{aire}=\frac{1}{2}\times13\times RH$','encre','m')
text(ax,66,qy+22,'contient le','varie','s');text(ax,66,qy+18,'sinus cherché','varie','s')
save(fig,'34-039')
