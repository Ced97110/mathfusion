import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
u=10; ox,oy=10,8
P=lambda a,b:(ox+a*u,oy+b*u)
poly(ax,[P(0,0),P(3,1),P(4,3),P(1,2)],'resultat')
arrow(ax,P(0,0),P(3,1),'sujet',lw=1.4); arrow(ax,P(0,0),P(1,2),'autre',lw=1.4)
text(ax,P(3,1)[0]+4,P(3,1)[1]-3,r'$u$','sujet','l'); text(ax,P(1,2)[0]-4,P(1,2)[1]+2,r'$v$','autre','l')
arrow(ax,(P(0,0)[0]+9,P(0,0)[1]+3.5),(P(0,0)[0]+3.5,P(0,0)[1]+9),'varie',curve=0.5)
text(ax,P(2,1.5)[0]+1,P(2,1.5)[1],'aire 5','resultat','m')
text(ax,72,40,'u ∧ v','resultat','xl')
text(ax,72,16,'sens inverse','varie','s')
text(ax,72,12,'des aiguilles','varie','s')
save(fig,'76-085')
