import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

fig,ax=canvas(72); s=14
a=(math.cos(math.radians(50)),math.sin(math.radians(50))); br=(-a[1],a[0]); bb=(a[1],-a[0])
def sq(o,b,role):
    p=lambda k,l:(o[0]+s*(k*a[0]+l*b[0]),o[1]+s*(k*a[1]+l*b[1]))
    poly(ax,[p(0,0),p(1,0),p(1,1),p(0,1)],role)
    arrow(ax,o,p(1,0),'encre',lw=1.4); arrow(ax,o,p(0,1),role,lw=1.4)
    return p
OL=(28,28); OR=(62,36)
pl=sq(OL,br,'sujet'); pr=sq(OR,bb,'varie')
arcarr(ax,OL,6,50,140,'sujet'); arcarr(ax,OR,6,50,-40,'varie')
text(ax,OL[0],65.5,'rotation','sujet','l',weight='bold'); text(ax,OR[0],65.5,'réflexion','varie','l',weight='bold')
text(ax,OL[0],60,'quart de tour en avant','sujet','s'); text(ax,OR[0],60,'quart de tour en arrière','varie','s')
text(ax,OL[0],10,'déterminant 1','sujet','m'); text(ax,OR[0],10,'déterminant −1','varie','m')
text(ax,OL[0]-1,OL[1]+11,'+90°','sujet','s'); text(ax,OR[0]+12,OR[1]+1,'−90°','varie','s')
t=pl(1,0); text(ax,t[0]+2,t[1]+3,'noir','encre','s',ha='left')
t=pr(1,0); text(ax,t[0]+2,t[1]+3,'noir','encre','s',ha='left')
t=pl(0,1); text(ax,t[0]-1,t[1]+4,r'$R(\theta)e_2$','sujet','s',ha='right')
t=pr(0,1); text(ax,t[0]+2,t[1]-4,r'$B(\theta)e_2$','varie','s',ha='left')
save(fig,'73-098')
