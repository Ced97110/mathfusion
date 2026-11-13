import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54); O=(46,10); s=9
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
poly(ax,[P(0,0),P(1,2),P(-1,3),P(-2,1)],'varie')
poly(ax,[P(0,0),P(1,0),P(1,1),P(0,1)],'sujet')
arrow(ax,P(0,0),P(1,2),'varie',lw=1.3); arrow(ax,P(0,0),P(-2,1),'varie',lw=1.3)
text(ax,P(1,2)[0]+2,P(1,2)[1]+1,r'$1+2i$','varie','m',ha='left')
text(ax,P(-2,1)[0]-2,P(-2,1)[1]-1,r'$-2+i$','varie','m',ha='right')
text(ax,P(1,0)[0]+3,P(1,0)[1]+4,'aire 1','sujet','m',ha='left')
text(ax,P(-0.5,1.9)[0],P(-0.5,1.9)[1],'aire 5','varie','l')
text(ax,44,48,'norme de $1+2i$ = 5','resultat','m')
save(fig,'76-141')
