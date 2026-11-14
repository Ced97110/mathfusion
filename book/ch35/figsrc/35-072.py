import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role='fixe',lw=0.9,dash=False):
    line(ax,[P(c,r,a0+(a1-a0)*i/48) for i in range(49)],role,lw,dash)
def mid(p,q): return ((p[0]+q[0])/2,(p[1]+q[1])/2)
def ra(ax,m,d1,d2,s=1.8,role='fixe'):
    n1=math.hypot(*d1); n2=math.hypot(*d2); u=(d1[0]/n1,d1[1]/n1); v=(d2[0]/n2,d2[1]/n2)
    line(ax,[(m[0]+s*u[0],m[1]+s*u[1]),(m[0]+s*(u[0]+v[0]),m[1]+s*(u[1]+v[1])),(m[0]+s*v[0],m[1]+s*v[1])],role,lw=0.7)
def tick(ax,p,q,n=1,role='fixe',s=1.2):
    m=mid(p,q); dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    for i in range(n):
        o=(i-(n-1)/2)*1.1
        c=(m[0]+ux*o,m[1]+uy*o); line(ax,[(c[0]-nx*s,c[1]-ny*s),(c[0]+nx*s,c[1]+ny*s)],role,lw=0.8)
def dot(ax,p,role,r=1.1): disc(ax,p[0],p[1],r,role)

fig,ax=canvas(84)
disc(ax,44,76,4.5,'sujet',label='M'); text(ax,52,76,'départ : le milieu','sujet','s',ha='left')
box(ax,3,38,40,26,'fixe'); text(ax,23,59,'Étape 1','fixe','m',weight='bold'); text(ax,23,51,r'$\frac{\cos P+\cos Q}{2}$','fixe','s'); text(ax,23,42,'par U et V','fixe','s')
box(ax,45,38,40,26,'varie',lw=1.8); text(ax,65,59,'Étape 2','varie','m',weight='bold'); text(ax,65,51,r'$\cos\frac{P-Q}{2}\cos\frac{P+Q}{2}$','varie','s'); text(ax,65,42,'par OMV : décisive','varie','s')
arrow(ax,(40,71),(23,65),'fixe'); arrow(ax,(48,71),(65,65),'varie')
box(ax,3,5,82,22,'resultat'); text(ax,44,22,'Étape 3 : égaler, puis × 2','resultat','m',weight='bold'); text(ax,44,12,r'$\cos P+\cos Q=2\cos\frac{P+Q}{2}\cos\frac{P-Q}{2}$','resultat','s')
arrow(ax,(23,38),(23,28),'fixe'); arrow(ax,(65,38),(65,28),'varie')
save(fig,'35-072')
