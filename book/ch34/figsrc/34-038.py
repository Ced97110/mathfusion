import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
s=3.5
ox,oy=4,16
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+2.9*s,oy+3*s,'30','sujet','l',weight='bold');text(ax,ox+8.5*s,oy+3*s,'54','varie','l',weight='bold')
brace(ax,P[0],N[0],oy-1,'sujet',label=r'$x=5$')
brace(ax,N[0],R[0],oy-1,'varie',label=r'$y=9$')
text(ax,N[0]+7,oy+8*s,r'$h=12$','encre','s')
text(ax,67,52,r'$\frac{xh}{2}=\frac{5\times12}{2}=30$','sujet','s')
text(ax,67,40,r'$\frac{yh}{2}=\frac{9\times12}{2}=54$','varie','s')
text(ax,67,26,r'$30+54=84$','resultat','m',weight='bold')
text(ax,67,20.5,'aire du grand triangle','resultat','s')
save(fig,'34-038')
