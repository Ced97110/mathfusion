import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
s=2.6
ox,oy=3,12
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
line(ax,[N,Q],'encre',lw=2.2)
text(ax,N[0]+2.5,oy+6*s,r'$h$','encre','m',weight='bold')
text(ax,ox+2.5*s,oy-3,r'$x$','sujet','s');text(ax,ox+1.9*s-1.5,oy+7*s,r'$r$','sujet','s')
text(ax,ox+11*s+1,oy+7*s,r'$p$','varie','s')
text(ax,N[0],oy-8,'h commun','encre','s') if False else None
text(ax,N[0],Q[1]+4,'h : côté commun','encre','s')
box(ax,42,40,44,13,'sujet',label=r'$\frac{x}{r}=\sin A$'+'\n'+'lu dans le triangle bleu')
box(ax,42,22,44,13,'varie',label=r'$\frac{h}{p}=\cos B$'+'\n'+'lu dans le triangle orange')
arrow(ax,(64,22),(64,15),'fixe')
box(ax,42,3,44,11,'resultat',label=r'$\sin A\cos B$ mêle A et B')
save(fig,'34-047')
