import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
s=2.5
ox,oy=3,10
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+2.5*s,oy-3,r'$x$','sujet','s');text(ax,ox+9.5*s,oy-3,r'$y$','varie','s')
text(ax,N[0]+2.2,oy+5*s,r'$h$','encre','s')
text(ax,ox+1.9*s-1.5,oy+7*s,r'$r$','sujet','s');text(ax,ox+11*s+1,oy+7*s,r'$p$','varie','s')
text(ax,Q[0]-3.5,Q[1]-10,r'$A$','sujet','s');text(ax,Q[0]+4.5,Q[1]-10,r'$B$','varie','s')
rows=[(r'$\sin A=\frac{x}{r}=\frac{5}{13}$','sujet'),(r'$\cos A=\frac{h}{r}=\frac{12}{13}$','sujet'),
      (r'$\sin B=\frac{y}{p}=\frac{9}{15}$','varie'),(r'$\cos B=\frac{h}{p}=\frac{12}{15}$','varie')]
for i,(t,role) in enumerate(rows):
    box(ax,42,40-i*11.5,44,10,role,label=t)
save(fig,'34-043')
