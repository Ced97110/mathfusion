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

fig,ax=canvas(74); O=(12,8); u=12
line(ax,[O,(76,8)],'fixe',lw=0.6); line(ax,[O,(12,72)],'fixe',lw=0.6)
arc(ax,O,5*u,0,90,'fixe',lw=0.8,dash=True); arc(ax,O,u,0,90,'sujet',lw=1.2)
Pt=(O[0]+0.6*u,O[1]+0.8*u); A=(O[0]+3*u,O[1]+4*u)
line(ax,[O,A],'fixe',lw=0.8)
arrow(ax,Pt,A,'varie',lw=1.2)
dot(ax,Pt,'sujet',1.4); dot(ax,A,'autre',1.6)
text(ax,O[0]-3.5,O[1]-3.5,'O','fixe','m')
text(ax,Pt[0]+2,Pt[1]-3.5,'(0,6 ; 0,8)','sujet','m',ha='left',weight='bold')
text(ax,A[0]+2.5,A[1]+2.5,'A(3 ; 4)','autre','m',ha='left',weight='bold')
mm=mid(Pt,A); text(ax,mm[0]+5,mm[1]-3,'× 5','varie','m',weight='bold')
text(ax,27,44,'même direction','fixe','s')
save(fig,'35-078')
