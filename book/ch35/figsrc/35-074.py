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

fig,ax=canvas(70); O=(10,18); r=46
arc(ax,O,r,-20,80,'fixe',lw=0.8); line(ax,[O,(60,18)],'fixe',lw=0.6)
U=P(O,r,75); line(ax,[O,U],'fixe',lw=0.7); dot(ax,U,'sujet',1.4)
text(ax,U[0]+2.5,U[1]+2.5,'U','sujet','m',weight='bold'); text(ax,O[0]-3.5,O[1]-3.5,'O','fixe','m')
for a,g,v in ((45,'30°','0,9659'),(15,'60°','0,866'),(-15,'90°','0,7071')):
    V=P(O,r,a); M=mid(U,V)
    line(ax,[U,V],'sujet',lw=1.1); line(ax,[O,M],'resultat',lw=1.3)
    dot(ax,V,'fixe',1.1); dot(ax,M,'resultat',1.2)
    line(ax,[(V[0]+2.5,V[1]),(60,V[1])],'fixe',lw=0.5,dash=True)
    text(ax,62,V[1]+2.3,'écart '+g,'fixe','s',ha='left'); text(ax,62,V[1]-2,'OM = '+v,'resultat','s',ha='left',weight='bold')
save(fig,'35-074')
