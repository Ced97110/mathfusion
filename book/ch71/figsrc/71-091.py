import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax,c,r,a0,a1,role,n=24):
    pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw=1.0); arrow(ax,pts[-2],pts[-1],role,lw=1.0)

fig,ax=canvas(60)
u=7; o=(8,12); xa=(3,1); ya=(1,2)
ang=lambda v: math.degrees(math.atan2(v[1],v[0]))
P=lambda v:(o[0]+v[0]*u,o[1]+v[1]*u)
poly(ax,[o,P(xa),P((4,3)),P(ya)],'sujet')
arrow(ax,o,P(xa),'sujet',lw=1.4); arrow(ax,o,P(ya),'varie',lw=1.4)
arc(ax,o,9,ang(xa),ang(ya),'varie'); arc(ax,o,13,ang(ya),ang(xa),'varie')
text(ax,P(xa)[0]+3,P(xa)[1]-3,r'$x$','sujet','m'); text(ax,P(ya)[0]-3,P(ya)[1]+3,r'$y$','varie','m')
text(ax,P((2.4,1.5))[0],P((2.4,1.5))[1],'aire 5','sujet','s')
text(ax,62,50,'de x vers y','encre','s'); text(ax,62,44,'sens inverse des aiguilles','encre','s'); text(ax,62,38,'signe +','encre','m')
text(ax,62,22,'de y vers x','encre','s'); text(ax,62,16,'sens des aiguilles','encre','s'); text(ax,62,10,'signe −','encre','m')
save(fig,'71-091')
