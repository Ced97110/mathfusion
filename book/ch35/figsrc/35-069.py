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

fig,ax=canvas(64); O=(10,8); r=50
arc(ax,O,r,0,90,'fixe'); line(ax,[O,(62,8)],'fixe',lw=0.6)
U=P(O,r,75); V=P(O,r,15); M=mid(U,V)
line(ax,[O,U],'fixe'); line(ax,[O,V],'fixe')
line(ax,[U,V],'sujet',lw=1.4); line(ax,[O,M],'resultat',lw=1.4)
ra(ax,M,(O[0]-M[0],O[1]-M[1]),(V[0]-M[0],V[1]-M[1]),3.6,'resultat')
arc(ax,O,34,0,75,'fixe',lw=0.9); arc(ax,O,22,0,15,'varie',lw=1.0)
for p in (U,V): dot(ax,p,'sujet',1.3)
dot(ax,M,'resultat',1.4)
text(ax,O[0]-3.5,O[1]-3.5,'O','fixe','m')
text(ax,U[0]+2.5,U[1]+2.5,'U','sujet','m',weight='bold'); text(ax,V[0]+3,V[1]+1,'V','sujet','m',weight='bold')
text(ax,M[0]+3,M[1]+2.5,'M','resultat','m',weight='bold'); text(ax,M[0]+9,M[1]-6,'90°','resultat','s')
q=P(O,38,70); text(ax,q[0]+3,q[1]-2,'P = 75°','fixe','s'); q=P(O,27,7.5); text(ax,q[0]+4,q[1]+1.5,'Q = 15°','varie','s')
text(ax,66,52,'OU = OV = 1','fixe','s'); text(ax,66,44,'OM = 0,866','resultat','s')
save(fig,'35-069')
