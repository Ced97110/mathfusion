import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52); O=(44,10); s=12
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
poly(ax,[P(0,0),P(1,1),P(0,2),P(-1,1)],'varie')
poly(ax,[P(0,0),P(1,0),P(1,1),P(0,1)],'sujet')
arrow(ax,P(0,0),P(1,0),'sujet',lw=1.3); arrow(ax,P(0,0),P(0,1),'sujet',lw=1.3)
arrow(ax,P(0,0),P(1,1),'varie',lw=1.3); arrow(ax,P(0,0),P(-1,1),'varie',lw=1.3)
text(ax,P(1,0)[0]+3,P(1,0)[1]-3,r'$v_1$','sujet','m'); text(ax,P(0,1)[0]+3,P(0,1)[1]-2,r'$v_2$','sujet','m')
text(ax,P(1,1)[0]+9,P(1,1)[1]+3,r'$v_1+v_2$','varie','m'); text(ax,P(-1,1)[0]-9,P(-1,1)[1]+3,r'$v_2-v_1$','varie','m')
text(ax,P(1,0.5)[0]+7,P(1,0.5)[1],'aire 1','sujet','m')
text(ax,P(0,1.65)[0],P(0,1.65)[1],'aire 2','varie','m')
text(ax,44,5,r'nouvelle base : $\times\,2$','resultat','l') if False else None
text(ax,44,47,r'produit $\times\,2$','resultat','l')
save(fig,'76-136')
