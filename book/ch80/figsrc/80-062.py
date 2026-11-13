import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
ox,oy,s=26,34,13
P=lambda a,b:(ox+a*s,oy+b*s)
poly(ax,[P(-1.9,-2.2),P(1.9,-2.2),P(1.9,2.2),P(-1.9,2.2)],'sujet')
line(ax,[P(-1.7,0),P(1.7,0)],'fixe'); line(ax,[P(0,-1.9),P(0,1.9)],'fixe')
disc(ax,ox,oy,1.2,'fixe')
for p in ((1,1),(-1.2,0.8),(0.6,-1.4)): disc(ax,*P(*p),1.0,'varie')
box(ax,54,22,30,13,'sujet',label=r'$1=V$',size='l')
text(ax,69,43,'tous les vecteurs','sujet','s')
text(ax,69,15,'le plus grand :','encre','s'); text(ax,69,9,'tous les autres','encre','s'); text(ax,69,4,'sont dedans','encre','s')
save(fig,'80-062')
