import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
s=2.4
ox,oy=4,52
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+2.5*s,oy-3,r'$x$','sujet','s');text(ax,ox+9.5*s,oy-3,r'$y$','varie','s')
text(ax,N[0]+2.2,oy+6*s,r'$h$','encre','s')
text(ax,ox+1.9*s-1,oy+7*s,r'$r$','sujet','s');text(ax,ox+11*s+1,oy+7*s,r'$p$','varie','s')
text(ax,66,oy+6,'départ','encre','m',weight='bold')
text(ax,66,oy+0.5,'deux triangles','encre','s')
arrow(ax,(44,48),(44,40),'fixe')
box(ax,4,22,80,16,'varie',label=r'$rp\,\sin(A+B)=xh+yh$'+'\n'+r'$13\times15\times\sin(A+B)=168$',size='m')
text(ax,44,43.5,'étape décisive','varie','s') if False else None
text(ax,70,43.5,'étape décisive','varie','s',ha='center')
arrow(ax,(44,22),(44,13),'fixe')
box(ax,4,0.5,80,11,'resultat',label=r'$\sin(A+B)=\frac{168}{195}=\frac{56}{65}$')
text(ax,70,17.5,'arrivée : division','resultat','s')
save(fig,'34-037')
