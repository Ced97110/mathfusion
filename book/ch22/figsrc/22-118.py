import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def G(sc,ox,oy): return lambda x,y:(ox+sc*x,oy+sc*y)
def curve(ax,g,fn,a,b,role,n=80,lw=1.2):
    pts=[g(a+(b-a)*i/n,fn(a+(b-a)*i/n)) for i in range(n+1)]; line(ax,pts,role,lw=lw)
def axes(ax,g,x0,x1,y0,y1):
    arrow(ax,g(x0,0),g(x1,0),'fixe',lw=0.8); arrow(ax,g(0,y0),g(0,y1),'fixe',lw=0.8)
def dot(ax,g,x,y,role,r=1.3): disc(ax,*g(x,y),r,role)
def lab(ax,g,x,y,s,role='encre',size='s',ha='center'): text(ax,*g(x,y),s,role,size,ha=ha)
fig,ax=canvas(48)
g=G(7.5,8,10)
axes(ax,g,-0.3,10.2,-0.3,4)
curve(ax,g,lambda x:x**0.5,0,9.8,'sujet')
for x in (1,4,9): line(ax,[g(x,0),g(x,x**0.5)],'fixe',dash=True)
for x in (0,1,4,9): dot(ax,g,x,x**0.5,'resultat')
lab(ax,g,-0.3,-0.6,r'$(0,\ 0)$','resultat',ha='left'); lab(ax,g,0.7,1.6,r'$(1,\ 1)$','resultat')
lab(ax,g,4,2.6,r'$(4,\ 2)$','resultat'); lab(ax,g,9,3.7,r'$(9,\ 3)$','resultat')
save(fig,'22-118')
