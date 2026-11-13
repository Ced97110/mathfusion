import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def G(sc,ox,oy): return lambda x,y:(ox+sc*x,oy+sc*y)
def curve(ax,g,fn,a,b,role,n=80,lw=1.2):
    pts=[g(a+(b-a)*i/n,fn(a+(b-a)*i/n)) for i in range(n+1)]; line(ax,pts,role,lw=lw)
def axes(ax,g,x0,x1,y0,y1):
    arrow(ax,g(x0,0),g(x1,0),'fixe',lw=0.8); arrow(ax,g(0,y0),g(0,y1),'fixe',lw=0.8)
def dot(ax,g,x,y,role,r=1.3): disc(ax,*g(x,y),r,role)
def lab(ax,g,x,y,s,role='encre',size='s',ha='center'): text(ax,*g(x,y),s,role,size,ha=ha)
fig,ax=canvas(80)
g=G(13,10,8)
axes(ax,g,-0.2,5.2,-0.2,5.2)
line(ax,[g(0,0),g(5,5)],'fixe',dash=True)
curve(ax,g,lambda x:x*x,0,2.25,'varie'); curve(ax,g,lambda x:x**0.5,0,5,'sujet')
for (a,b) in ((2,4),(4,2)):
    line(ax,[g(a,0),g(a,b)],'fixe',dash=True); line(ax,[g(0,b),g(a,b)],'fixe',dash=True)
dot(ax,g,2,4,'varie'); dot(ax,g,4,2,'sujet')
lab(ax,g,2.2,4.3,r'$Q(2,\ 4)$','varie',ha='left'); lab(ax,g,4.2,1.6,r'$P(4,\ 2)$','sujet',ha='left')
for v in (2,4): lab(ax,g,v,-0.45,str(v),'fixe'); lab(ax,g,-0.4,v,str(v),'fixe')
lab(ax,g,1.0,4.6,r'$y = x^2$','varie'); lab(ax,g,4.4,0.6,r'$y=\sqrt{x}$','sujet')
save(fig,'22-122')
