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

fig,ax=canvas(58); f=numberline(ax,10,78,30,0,90,step=15,every=2,arrow_right=False)
line(ax,[(f(15),30),(f(75),30)],'fixe',lw=1.6)
for v,n in ((15,'Q = 15°'),(75,'P = 75°')):
    dot(ax,(f(v),30),'fixe',1.4); text(ax,f(v),35,n,'fixe','m')
disc(ax,f(45),30,1.9,'sujet'); text(ax,f(45),44,r'$(P+Q)/2=45^\circ$','sujet','l',weight='bold')
line(ax,[(f(45),32.5),(f(45),41)],'sujet',dash=True)
text(ax,44,10,r'$75+15=90$','fixe','m'); text(ax,44,4.5,r'$90\div 2=45$','sujet','m')
save(fig,'35-066')
