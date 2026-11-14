import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def G(sc,ox,oy): return lambda x,y:(ox+sc*x,oy+sc*y)
def curve(ax,g,fn,a,b,role,n=80,lw=1.2):
    pts=[g(a+(b-a)*i/n,fn(a+(b-a)*i/n)) for i in range(n+1)]; line(ax,pts,role,lw=lw)
def axes(ax,g,x0,x1,y0,y1):
    arrow(ax,g(x0,0),g(x1,0),'fixe',lw=0.8); arrow(ax,g(0,y0),g(0,y1),'fixe',lw=0.8)
def dot(ax,g,x,y,role,r=1.3): disc(ax,*g(x,y),r,role)
def lab(ax,g,x,y,s,role='encre',size='s',ha='center'): text(ax,*g(x,y),s,role,size,ha=ha)
fig,ax=canvas(84)
g=G(14,10,8)
axes(ax,g,-0.2,5.2,-0.2,5.2)
line(ax,[g(0,0),g(5,5)],'fixe')
lab(ax,g,4.4,4.9,r'$y = x$','fixe')
dot(ax,g,2,4,'sujet'); dot(ax,g,4,2,'resultat'); dot(ax,g,1,1,'fixe')
arrow(ax,(g(2,4)[0]+1.8,g(2,4)[1]-1.8),(g(4,2)[0]-1.8,g(4,2)[1]+1.8),'varie')
lab(ax,g,2.2,4.3,r'$(2,\ 4)$','sujet',ha='left'); lab(ax,g,4.2,1.6,r'$(4,\ 2)$','resultat',ha='left')
lab(ax,g,1.2,0.6,r'$(1,\ 1)$ reste','fixe',ha='left')
lab(ax,g,4.15,3.1,'échange','varie')
save(fig,'22-123')
