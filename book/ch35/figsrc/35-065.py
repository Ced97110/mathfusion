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

fig,ax=canvas(72); O=(10,8)
line(ax,[O,P(O,60,0)],'fixe')
line(ax,[O,P(O,52,75)],'fixe',lw=1.2)
line(ax,[O,P(O,56,15)],'sujet',lw=1.3)
arc(ax,O,20,0,15,'sujet',lw=1.3); arc(ax,O,30,0,75,'fixe')
a=P(O,52,75); b=P(O,56,15)
text(ax,a[0]+2,a[1]+1,'P = 75°','fixe','m',ha='left')
text(ax,b[0]+2,b[1]+1,'Q = 15°','sujet','m',ha='left',weight='bold')
text(ax,46,12.5,'second angle','sujet','s')
text(ax,22,66,r'$\sin 75^\circ$','fixe','l'); text(ax,44,66,'+','encre','l'); text(ax,64,66,r'$\sin 15^\circ$','sujet','l',weight='bold')
save(fig,'35-065')
