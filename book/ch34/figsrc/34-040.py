import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
s=2.4
ox,oy=4,34
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+7*s,oy-4,r'$\frac{xh}{2}+\frac{yh}{2}=84$','resultat','s')
qx,qy=52,34
Qq=(qx,qy);Pp=(qx+13*s,qy);Rr=(qx+7.615*s,qy+12.923*s)
poly(ax,[Qq,Pp,Rr],'fixe')
line(ax,[Rr,(Rr[0],qy)],'varie',lw=1.1,dash=True)
text(ax,qx+6.5*s,qy-4,r'$\frac{rp}{2}\sin(A+B)\approx84$','resultat','s')
text(ax,44,oy+6*s,'=','resultat','xl',weight='bold')
text(ax,44,oy+12*s+8,'un seul triangle, une seule aire','encre','s') if False else None
text(ax,44,oy+12*s+7,'même triangle, même aire','encre','s')
arrow(ax,(44,oy-6),(44,18.5),'varie')
text(ax,50,oy-12.5,'× 2','varie','s')
box(ax,4,5,80,12,'resultat',label=r'$rp\,\sin(A+B)=xh+yh$')
save(fig,'34-040')
