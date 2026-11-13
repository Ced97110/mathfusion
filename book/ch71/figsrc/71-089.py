import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax,c,r,a0,a1,role,n=24):
    pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw=1.0); arrow(ax,pts[-2],pts[-1],role,lw=1.0)

fig,ax=canvas(52)
u=6.5; xa=(3,1); ya=(1,2)
ang=lambda v: math.degrees(math.atan2(v[1],v[0]))
for ox,first,second,fr,sr,val,a0,a1 in ((4,xa,ya,'sujet','varie',r'$B(x,y)=5$',ang(xa),ang(ya)),(48,ya,xa,'varie','sujet',r'$B(y,x)=-5$',ang(ya),ang(xa))):
    o=(ox,10)
    P=lambda v: (o[0]+v[0]*u,o[1]+v[1]*u)
    poly(ax,[o,P(xa),P((4,3)),P(ya)],'fixe')
    arrow(ax,o,P(xa),'sujet',lw=1.4); arrow(ax,o,P(ya),'varie',lw=1.4)
    arc(ax,o,9,a0,a1,'varie')
    text(ax,o[0]+u*3+3,o[1]+u*1-3,r'$x$','sujet','m'); text(ax,o[0]+u*1-3,o[1]+u*2+3,r'$y$','varie','m')
    text(ax,o[0]+18,45,val,'encre','m')
text(ax,44,6,'même parallélogramme','fixe','s')
save(fig,'71-089')
