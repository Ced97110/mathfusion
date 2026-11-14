import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
s=2.2
ox,oy=3,36
P=(ox,oy);N=(ox+5*s,oy);R=(ox+14*s,oy);Q=(ox+5*s,oy+12*s)
poly(ax,[P,N,Q],'sujet');poly(ax,[N,R,Q],'varie')
text(ax,ox+2.8*s,oy+3*s,'30','sujet','m');text(ax,ox+8.5*s,oy+3*s,'54','varie','m')
text(ax,62,oy+18,'côte à côte :','resultat','s');text(ax,62,oy+12,r'$30+54=84$','resultat','m',weight='bold')
text(ax,62,oy+6,'le signe est +','resultat','s')
line(ax,[(4,31),(84,31)],'fixe',dash=True)
text(ax,44,27,'avec un recouvrement','encre','s')
k=0.8; y=9
box(ax,4,y,30*k,8,'sujet',r=0.4)
box(ax,4+20*k,y,54*k,8,'varie',r=0.4)
box(ax,4+20*k,y,10*k,8,'fixe',label='10',r=0.4,size='s')
text(ax,4+8*k,y+4,'30','sujet','s')
text(ax,4+48*k,y+4,'54','varie','s')
brace(ax,4,4+74*k,y+9,'fixe',label=r'$30+54-10=74$',down=False)
save(fig,'34-046')
