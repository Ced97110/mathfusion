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

fig,ax=canvas(80); O=(12,8); r=46
text(ax,12,71,'2','sujet','xl',weight='bold'); text(ax,19,71,'×','encre','l')
text(ax,36,71,r'$\cos\frac{P+Q}{2}$','varie','l'); text(ax,52,71,'×','encre','l'); text(ax,70,71,r'$\cos\frac{P-Q}{2}$','resultat','l')
arc(ax,O,r,0,90,'fixe',lw=0.8); line(ax,[O,(62,8)],'fixe',lw=0.6)
U=P(O,r,75); V=P(O,r,15); M=mid(U,V)
line(ax,[O,U],'fixe'); line(ax,[O,V],'fixe'); line(ax,[U,V],'fixe',lw=1.0)
line(ax,[O,M],'resultat',lw=1.6); arc(ax,O,22,0,45,'varie',lw=1.6)
for p in (U,V): dot(ax,p,'fixe',1.2)
dot(ax,M,'sujet',1.8)
text(ax,O[0]-3.5,O[1]-3.5,'O','fixe','m'); text(ax,U[0]+2.5,U[1]+2.5,'U','fixe','m'); text(ax,V[0]+3,V[1]+1,'V','fixe','m')
text(ax,M[0]+3,M[1]+3,'M','sujet','m',weight='bold')
text(ax,71,56,'milieu M :\nfacteur 2','sujet','s'); text(ax,72,43,'OM = 0,866 :\ndistance','resultat','s'); text(ax,72,31,'direction de OM : 45°','varie','s')
save(fig,'35-073')
