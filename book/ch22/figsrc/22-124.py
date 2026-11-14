import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def G(sc,ox,oy): return lambda x,y:(ox+sc*x,oy+sc*y)
def curve(ax,g,fn,a,b,role,n=80,lw=1.2):
    pts=[g(a+(b-a)*i/n,fn(a+(b-a)*i/n)) for i in range(n+1)]; line(ax,pts,role,lw=lw)
def axes(ax,g,x0,x1,y0,y1):
    arrow(ax,g(x0,0),g(x1,0),'fixe',lw=0.8); arrow(ax,g(0,y0),g(0,y1),'fixe',lw=0.8)
def dot(ax,g,x,y,role,r=1.3): disc(ax,*g(x,y),r,role)
def lab(ax,g,x,y,s,role='encre',size='s',ha='center'): text(ax,*g(x,y),s,role,size,ha=ha)
fig,ax=canvas(90)
g=G(7.4,6,6)
axes(ax,g,-0.3,10.2,-0.3,10.2)
line(ax,[g(0,0),g(10,10)],'fixe',dash=True)
curve(ax,g,lambda x:x*x,0,3.16,'varie'); curve(ax,g,lambda x:x**0.5,0,10,'sujet')
dot(ax,g,3,9,'varie'); dot(ax,g,9,3,'sujet')
p=g(3,9); q=g(9,3); s=1.8*0.7071
arrow(ax,(p[0]+s,p[1]-s),(q[0]-s,q[1]+s),'resultat')
lab(ax,g,2.8,9,r'$(3,\ 9)$','varie',ha='right'); lab(ax,g,9,2.2,r'$(9,\ 3)$','sujet')
lab(ax,g,1.1,9.9,r'$y = x^2$','varie'); lab(ax,g,6.5,4.2,r'$y=\sqrt{x}$','sujet')
lab(ax,g,8.2,9.5,r'$y = x$','fixe'); lab(ax,g,7.7,5.9,'reflet','resultat')
save(fig,'22-124')
